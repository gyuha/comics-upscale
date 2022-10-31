from functools import reduce
import os
import pathlib
import re
from enum import Enum
import uuid

from PySide6 import QtCore, QtGui
from PySide6.QtCore import QObject, QSize, Qt, QThread, Signal, Slot
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QIcon

import MainWindow
from util.ImageOptimize import ImageOptimize
from util.Zip import Zip
from util.Unzip import Unzip
from util.Config import Config
from util.Upscaler import UpscaleType, Upscaler
from ui.ui_UpscaleItem import Ui_UpscaleItem


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
        self._parent = parent

        self.ui = Ui_UpscaleItem()
        self.ui.setupUi(self)

        self.id = str(uuid.uuid4())
        self.file_path = file_path
        self.base_name = os.path.basename(file_path)
        self.dir_name = os.path.dirname(file_path)

        self.is_done = False
        self.total_count = 0

        self.state = ItemState.READY

        self._init_text()
        self._init_connect()
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
        if self.re_image.search(file_path) != None:
            self.upscale_type = UpscaleType.COMPRESS_IMAGE
        self.upscaler.signals.upscale_state.connect(self._on_upscale_state)

        self.signals.run.connect(self._on_run)

    def _init_connect(self):
        self.ui.btn_run.clicked.connect(self._on_click_run)

    def _init_text(self):
        self.ui.lbl_file_name.setText(self.base_name)
        self.ui.lbl_path.setText(self.dir_name)
        self.ui.pgb_progress.setValue(0)
        self.ui.lbl_state.setText("Ready")

    def _set_run_icon(self, type: str):
        icon = QIcon()
        icon.addFile(f":/icon/icons/{type}.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.btn_run.setIcon(icon)

    def _on_click_run(self):
        if self.state == ItemState.READY:
            self._set_run_icon("stop")
            self.state = ItemState.DOING
            self.ui.lbl_state.setText("Doing")
            self.upscaler.set(self.upscale_type, [self.file_path])
            print('📢[UpscaleItem.py:102]: ', self.id)
            print('📢[UpscaleItem.py:102]: ', type(self.id))
            self.signals.run.emit(self.id)
        else:
            self.state = ItemState.READY
            self._set_run_icon("play")
    
    @Slot(str)
    def _on_run(self, id: str):
        print('📢[UpscaleItem.py:109]: ', id)
        print('📢[UpscaleItem.py:110]: ', self.id)
        if self.id != id:
            return
        if self.upscale_type == UpscaleType.IMAGE:
            self.upscaler.start()
        else:
            self.unzip.start()

    @Slot(str, bool, int, int)
    def _on_unzip_state(self, id: str, complete: bool, current: int, total: int):
        if self.id != id:
            return

        self.ui.lbl_state.setText(f"Unzip files [{current}/{total}]")
        if total > 0:
            self.ui.pgb_progress.setValue(current / total * 100)

        if complete:
            # 이미지 업스케일 시작 하기
            self.ui.lbl_state.setText("Unzip Complete")
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

        self.ui.lbl_state.setText(f"Upscaling [{current}/{total}]")
        self.ui.pgb_progress.setValue(percent)
        if complete:
            self.ui.btn_run.setDisabled(True)
            self.ui.lbl_state.setText("Upscaling Complete")
            self.optimize.start()
    

    @Slot(str, bool, int, int)
    def _on_optimize_state(self, id: str, complete: bool, current: int, total: int):
        if self.id != id:
            return

        self.ui.lbl_state.setText(f"JPG Optimize [{current}/{total}]")
        if total > 0:
            self.ui.pgb_progress.setValue(current / total * 100)

        if complete:
            self.ui.lbl_state.setText("Optimize Completed")
            self.zip.start()

    @Slot(str, bool, int, int)
    def _on_zip_state(self, id: str, complete: bool, current: int, total: int):
        if self.id != id:
            return

        self.ui.lbl_state.setText(f"Zip files [{current}/{total}]")
        if total > 0:
            self.ui.pgb_progress.setValue(current / total * 100)

        if complete:
            self.state = ItemState.DONE
            self.ui.btn_run.setDisabled(True)
            self.ui.lbl_state.setText("Completed")
            self.ui.lbl_state.setStyleSheet("color: blue")
    