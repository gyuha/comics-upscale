from enum import Enum
import os
import pathlib
import re
from PySide6.QtWidgets import QWidget
from PySide6 import QtGui, QtCore
from PySide6.QtCore import QObject, QThread, Signal, Slot, QSize, Qt

import MainWindow
from ui.ui_UpscaleItem import Ui_UpscaleItem

class UpscaleItem(QWidget):

    def __init__(self, parent: MainWindow, file_path: str):
        super(UpscaleItem, self).__init__()
        self._parent = parent

        self.ui = Ui_UpscaleItem()
        self.ui.setupUi(self)

        self.file_path = file_path
        print('📢[UpscaleItem.py:22]: ', str)

        self._init_text()

    
    def _init_text(self):
        self.ui.lbl_file_name.setText(self.file_path)
        self.ui.lbl_path.setText(self.file_path)