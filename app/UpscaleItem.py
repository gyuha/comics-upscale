import os
import pathlib
import re
from enum import Enum

from PySide6 import QtCore, QtGui
from PySide6.QtCore import QObject, QSize, Qt, QThread, Signal, Slot
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QIcon

import MainWindow
from util.Upscaler import Upscaler
from ui.ui_UpscaleItem import Ui_UpscaleItem


class ItemState(Enum):
    READY = 1
    DOING = 2
    DONE = 3
    ERROR = 4


class UpscaleItem(QWidget):
    def __init__(self, parent: MainWindow, file_path: str):
        super(UpscaleItem, self).__init__()
        self._parent = parent

        self.ui = Ui_UpscaleItem()
        self.ui.setupUi(self)

        self.file_path = file_path
        self.base_name = os.path.basename(file_path)
        self.dir_name = os.path.dirname(file_path)

        self.is_done = False
        self.total_count = 0

        self.state = ItemState.READY

        self._init_text()
        self._init_connect()
        self.upscaler = Upscaler(self)

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
            self.upscaler.start(self.file_path, [self.file_path])
        else: 
            self.state = ItemState.READY
            self._set_run_icon("play")
