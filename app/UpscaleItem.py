from functools import reduce
import os
import pathlib
import re
from enum import Enum

from PySide6 import QtCore, QtGui
from PySide6.QtCore import QObject, QSize, Qt, QThread, Signal, Slot
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QIcon

import MainWindow
from util.Config import Config
from util.Upscaler import UpscaleType, Upscaler
from ui.ui_UpscaleItem import Ui_UpscaleItem


class ItemState(Enum):
    READY = 1
    DOING = 2
    DONE = 3
    ERROR = 4

class UpscaleItemSignal(QObject):
    run = Signal()


class UpscaleItem(QWidget):
    signals = UpscaleItemSignal()

    def __init__(self, parent: MainWindow, file_path: str):
        super(UpscaleItem, self).__init__()
        self._parent = parent

        self.ui = Ui_UpscaleItem()
        self.ui.setupUi(self)

        self.id = file_path
        self.file_path = file_path
        self.base_name = os.path.basename(file_path)
        self.dir_name = os.path.dirname(file_path)

        self.is_done = False
        self.total_count = 0

        self.state = ItemState.READY

        self._init_text()
        self._init_connect()
        self.upscaler = Upscaler(self)
        self.config = Config()

        image_re = re.compile(
            "\.("
            + reduce(lambda x, y: x + "|" + y, self.config.data["allow_image"])
            + ")$"
        )

        self.upscale_type = UpscaleType.IMAGE
        if image_re.search(file_path) == None:
            self.upscale_type = UpscaleType.COMPRESS_IMAGE
        self.upscaler.signals.upscale_state.connect(self._on_progress)

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
            self.upscaler.set(self.file_path, self.upscale_type, [self.file_path])
            self.signals.run.emit()
        else:
            self.state = ItemState.READY
            self._set_run_icon("play")
    
    @Slot()
    def _on_run(self):
        print('📢[UpscaleItem.py:92] START')
        self.upscaler.start()

    @Slot(str, bool, int, int)
    def _on_progress(self, id: str, complete: bool, current: int, total: int):
        if self.id != id or total == 0:
            return

        percent = current / total * 100

        self.ui.pgb_progress.setValue(current / total * 100)
        if complete:
            self.ui.btn_run.setDisabled(True)
            self.ui.lbl_state.setText("Complete")
