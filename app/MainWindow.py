from ast import List
from datetime import datetime
from enum import Enum
from functools import reduce
from genericpath import isdir
import os
import re

from PySide6.QtCore import Qt
from PySide6 import QtCore, QtGui
from PySide6.QtCore import QTime, QTimer, QDate
from PySide6.QtGui import QDropEvent, QDragMoveEvent, QDragEnterEvent
from PySide6.QtWidgets import QListWidgetItem, QMainWindow
from ItemStateWorker import ItemStateWorker
from constant.SettingEnum import SettingEnum
from pathlib import Path

from lib.Config import Config
from ui.ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.config = Config()
        self._load_config()

        self._init_connect()
        self.itemState = ItemStateWorker(self)
        self.itemState.start()

        self._re_allow_file = re.compile(
            "\.("
            + reduce(lambda x, y: x + "|" + y, self.config.data["allow_file"])
            + ")$"
        )

    def _init_connect(self):
        self.ui.cmb_format.activated.connect(self._save_config)
        self.ui.cmb_tile_size.activated.connect(self._save_config)
        self.ui.chb_tta_mode.stateChanged.connect(self._save_config)
        self.ui.cmb_upscale_ratio.activated.connect(self._save_config)
        self.ui.cmb_model_name.activated.connect(self._save_config)
        self.ui.cmb_jpg_optimize.activated.connect(self._save_config)

        self.ui.lst_item_list.setDragEnabled(True)
        self.ui.lst_item_list.setAcceptDrops(True)
        self.ui.lst_item_list.dragEnterEvent = self._on_list_drag_enter
        self.ui.lst_item_list.dragMoveEvent = self._on_list_drag_move
        self.ui.lst_item_list.dropEvent = self._on_list_drop
        # self.destroy.connect(self._on_destory)

        self.ui.btn_start.clicked.connect(self._on_click_start)

    def _save_config(self):
        self.config.setting[SettingEnum.FORMAT] = self.ui.cmb_format.currentText()
        self.config.setting[SettingEnum.TILE_SIZE] = self.ui.cmb_tile_size.currentText()
        self.config.setting[SettingEnum.TTA_MODE] = (
            True
            if self.ui.chb_tta_mode.checkState() == Qt.CheckState.Checked
            else False
        )
        self.config.setting[
            SettingEnum.UPSCALE_RATIO
        ] = self.ui.cmb_upscale_ratio.currentText()
        self.config.setting[
            SettingEnum.MODEL_NAME
        ] = self.ui.cmb_model_name.currentText()
        self.config.setting[
            SettingEnum.JPG_OPTIMIZE
        ] = self.ui.cmb_jpg_optimize.currentText()
        self.config.save()

    def _load_config(self):
        self.ui.cmb_format.setCurrentText(self.config.setting[SettingEnum.FORMAT])
        self.ui.cmb_tile_size.setCurrentText(self.config.setting[SettingEnum.TILE_SIZE])
        self.ui.chb_tta_mode.setCheckState(
            Qt.CheckState.Checked
            if self.config.setting[SettingEnum.TTA_MODE] == True
            else Qt.CheckState.Unchecked
        )
        self.ui.cmb_upscale_ratio.setCurrentText(
            self.config.setting[SettingEnum.UPSCALE_RATIO]
        )
        self.ui.cmb_model_name.setCurrentText(
            self.config.setting[SettingEnum.MODEL_NAME]
        )
        self.ui.cmb_jpg_optimize.setCurrentText(
            self.config.setting[SettingEnum.JPG_OPTIMIZE]
        )

    def _on_click_start(self):
        self._check_file_type("test")

    def _on_list_drag_enter(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def _on_list_drag_move(self, event: QDragMoveEvent):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def _on_list_drop(self, event: QDropEvent):
        lines = []
        for url in event.mimeData().urls():
            lines.append(url.toLocalFile())
        self._add_items(lines)

    def _check_file_type(self, file_path):
        t = self._re_allow_file.search(file_path)
        return t != None

    def _add_items(self, items):
        for i, item in enumerate(items):
            if not os.path.exists(item):
                continue

            if os.path.isfile(item):
                print("📢[MainWindow.py:92]: file => ", item)
                print('📢[MainWindow.py:131]: ', self._check_file_type(item))

            if os.path.isdir(item):
                print("📢[MainWindow.py:92]:  => ", item)

    def closeEvent(self, event):
        self.itemState.stop()
