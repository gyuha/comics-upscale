import os
from pathlib import Path
import shutil
import signal
import uuid
from enum import Enum

from PySide6.QtCore import QObject, QSize, Qt, QThread, Signal, Slot
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget

import MainWindow
from ui.ui_UpscaleItem import Ui_UpscaleItem
from util.Config import Config
from util.ImageOptimize import ImageOptimize
from util.message import toast
from util.Unzip import Unzip
from util.Upscaler import Upscaler, UpscaleType
from util.Zip import Zip


class ItemState(Enum):
    READY = 1
    DOING = 2
    DONE = 3
    ERROR = 4


class DoingState(Enum):
    UNZIP = 1
    UPSCALE = 2
    OPTIMIZE = 3
    ZIP = 3


class UpscaleItemSignal(QObject):
    run = Signal(str)


class UpscaleItem(QWidget):
    signals = UpscaleItemSignal()

    def __init__(self, parent: MainWindow, file_path: str):
        super(UpscaleItem, self).__init__()
        self._parent: MainWindow = parent

        self.ui = Ui_UpscaleItem()
        self.ui.setupUi(self)

        self.id = str(uuid.uuid4())
        self.file_path = file_path
        self.base_name = os.path.basename(file_path)
        self.dir_name = os.path.dirname(file_path)

        self.is_done = False
        self.total_count = 0

        self.state = ItemState.READY

        self.upscaler = Upscaler(self, self.id)
        self.config = Config()
        self.temp_dir = self.config.data["temp_dir"]

        self.unzip = Unzip(self, self.id, self.file_path)
        self.unzip.signals.unzip_state.connect(self._on_unzip_state)

        self.zip = Zip(self, self.id, self.file_path)
        self.zip.signals.zip_state.connect(self._on_zip_state)

        self.optimize = ImageOptimize(self, self.id)
        self.optimize.signals.optimize_state.connect(self._on_optimize_state)

        self.re_image = self.config.re_image_extension()

        self.upscale_type = UpscaleType.IMAGE
        if self.config.re_zip_extension().search(file_path):
            self.upscale_type = UpscaleType.COMPRESS_IMAGE

        self.target_path = self.config.replace_name(self.file_path)
        self.target_base_name = os.path.basename(self.target_path)

        self.upscaler.signals.upscale_state.connect(self._on_upscale_state)

        self.signals.run.connect(self._on_run)

        self._init_text()
        self._init_connect()

    def _init_connect(self):
        self.ui.btn_run.clicked.connect(self.on_click_run)
        self.ui.btn_delete.clicked.connect(self._on_click_remove)
        self.ui.btn_open_folder.clicked.connect(self._on_click_open_folder)

    def _init_text(self):
        item_name = self.base_name
        if self.base_name != self.target_base_name:
            item_name += f"  =>>  {self.target_base_name}"
        self.ui.lbl_file_name.setText(item_name)
        self.ui.lbl_path.setText(self.dir_name)
        self.ui.pgb_progress.setValue(0)
        self.ui.lbl_state.setText(self.tr("Ready"))

    def _set_run_icon(self, type: str):
        icon = QIcon()
        icon.addFile(f":/icon/icons/{type}.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.btn_run.setIcon(icon)

    def on_click_run(self):
        if self.state == ItemState.READY:
            msg = self.tr("An item is already running.")
            if self._parent.check_doing_item():
                toast(self, msg)
                return
            self._set_run_icon("stop")

            self.state = ItemState.DOING
            self.ui.lbl_state.setText(msg)

            self.signals.run.emit(self.id)
            self._parent.signals.item_state_change.emit(
                self.id, self.file_path, self.state
            )
        else:
            self.state = ItemState.READY
            self._set_run_icon("play")

    @Slot(str)
    def _on_run(self, id: str):
        if self.id != id:
            return
        if self.upscale_type == UpscaleType.IMAGE:
            self.upscaler.set(self.upscale_type, [self.file_path], self.target_path)
            self.upscaler.start()
        else:
            self.unzip.start()

    @Slot(str, bool, int, int)
    def _on_unzip_state(self, id: str, complete: bool, current: int, total: int):
        if self.id != id:
            return

        self.ui.lbl_state.setText(self.tr(f"Unzip files") + f" [{current}/{total}]")
        if total > 0:
            self.ui.pgb_progress.setValue(current / total * 100)

        if complete:
            # 이미지 업스케일 시작 하기
            self.ui.lbl_state.setText(self.tr("Unzip Complete"))
            files = os.listdir(self.temp_dir)
            files = list(filter(self.re_image.search, files))
            files = list(map(lambda x: os.path.join(self.temp_dir, x), files))
            self.upscaler.set(UpscaleType.COMPRESS_IMAGE, files)
            self.upscaler.start()

    @Slot(str, bool, int, int)
    def _on_upscale_state(self, id: str, complete: bool, current: int, total: int):
        if self.id != id or total == 0:
            return

        percent = 0
        if total > 0:
            percent = current / total * 100

        self.ui.lbl_state.setText(self.tr("Upscaling") + f" [{current}/{total}]")
        self.ui.pgb_progress.setValue(percent)
        if complete:
            if self.upscale_type == UpscaleType.IMAGE:
                self._on_complete()
            else:
                self.ui.btn_run.setDisabled(True)
                self.ui.lbl_state.setText(self.tr("Upscaling Complete"))
                self.optimize.start()

    @Slot(str, bool, int, int)
    def _on_optimize_state(self, id: str, complete: bool, current: int, total: int):
        if self.id != id:
            return

        self.ui.lbl_state.setText(self.tr("JPG Optimize") + f"[{current}/{total}]")
        if total > 0:
            self.ui.pgb_progress.setValue(current / total * 100)

        if complete:
            self.ui.lbl_state.setText(self.tr("Optimize Completed"))
            self.zip.start()

    @Slot(str, bool, int, int)
    def _on_zip_state(self, id: str, complete: bool, current: int, total: int):
        if self.id != id:
            return

        self.ui.lbl_state.setText(self.tr("Zip files" + f" [{current}/{total}]"))
        if total > 0:
            self.ui.pgb_progress.setValue(current / total * 100)

        if complete:
            self._on_complete()

    def _on_complete(self):
        self.state = ItemState.DONE
        self.ui.btn_run.setDisabled(True)
        self.ui.lbl_state.setText(self.tr("Completed"))
        self.ui.lbl_state.setStyleSheet("color: blue")
        self._remove_temp_folder()
        self._parent.signals.item_state_change.emit(self.id, self.file_path, self.state)

    def _remove_temp_folder(self):
        temp_dir = Path(self.config.data["temp_dir"]).absolute()
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)

    def _on_click_open_folder(self):
        if os.path.exists(self.dir_name):
            os.startfile(self.dir_name)

    def _on_click_remove(self):
        if self._parent.state == MainWindow.MainState.START:
            self.state = ItemState.DONE
            self._parent.start_next()
        else:
            self.state = ItemState.READY
        self._parent.signals.item_remove.emit(self.id, self.file_path)

    def btn_start_enable(self, value: bool):
        self.ui.btn_run.setEnabled(value)
