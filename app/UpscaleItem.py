from enum import Enum
import os
import pathlib
import re
from PySide6.QtWidgets import QWidget
from PySide6 import QtGui, QtCore
from PySide6.QtCore import QObject, QThread, Signal, Slot, QSize, Qt

from MainWindow import MainWindow

class UpscaleItem(QWidget):

    def __init__(self, parent: MainWindow, id: str):
        super(UpscaleItem, self).__init__()
        self._parent = parent