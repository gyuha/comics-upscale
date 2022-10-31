import os
import re
from ast import List
from datetime import datetime
from enum import Enum
from functools import reduce
from pathlib import Path

from genericpath import isdir
from PySide6 import QtCore, QtGui
from PySide6.QtCore import QDate, Qt, QTime, QTimer
from PySide6.QtGui import QDragEnterEvent, QDragMoveEvent, QDropEvent
from PySide6.QtWidgets import QListWidgetItem, QMainWindow
from lib.QToaster import QToaster

from constant.SettingEnum import SettingEnum
from ItemStateWorker import ItemStateWorker
from ui.ui_MainWindow import Ui_MainWindow
from UpscaleItem import UpscaleItem
from util.Config import Config


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

        self.item_dict: dict[str, QListWidgetItem] = {}

        self._re_allow_file = self.config.re_allow_extension()

        self.ui.lst_item_list.setStyleSheet(
            "QListWidget::item { border-bottom: 1px solid #eee; }"
        )

    def _init_connect(self):
        self.ui.cmb_format.activated.connect(self._save_config)
        self.ui.cmb_tile_size.activated.connect(self._save_config)
        self.ui.chb_tta_mode.stateChanged.connect(self._save_config)
        self.ui.chb_replace_origin.stateChanged.connect(self._save_config)
        self.ui.cmb_upscale_ratio.activated.connect(self._save_config)
        self.ui.cmb_model_name.activated.connect(self._save_config)
        self.ui.cmb_jpg_optimize.activated.connect(self._save_config)

        self.ui.lst_item_list.setDragEnabled(True)
        self.ui.lst_item_list.setAcceptDrops(True)
        self.ui.lst_item_list.dragEnterEvent = self._on_list_drag_enter
        self.ui.lst_item_list.dragMoveEvent = self._on_list_drag_move
        self.ui.lst_item_list.dropEvent = self._on_list_drop

        # buttons
        self.ui.btn_start.clicked.connect(self._on_click_start)
        self.ui.btn_list_clear.clicked.connect(self._on_click_list_clear)

    def _save_config(self):
        self.config.setting[SettingEnum.FORMAT] = self.ui.cmb_format.currentText()
        self.config.setting[SettingEnum.TILE_SIZE] = self.ui.cmb_tile_size.currentText()
        self.config.setting[SettingEnum.TTA_MODE] = (
            True
            if self.ui.chb_tta_mode.checkState() == Qt.CheckState.Checked
            else False
        )
        self.config.setting[SettingEnum.REPLACE_ORIGIN] = (
            True
            if self.ui.chb_replace_origin.checkState() == Qt.CheckState.Checked
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
        self.ui.chb_replace_origin.setCheckState(
            Qt.CheckState.Checked
            if self.config.setting[SettingEnum.REPLACE_ORIGIN] == True
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

    def _on_click_list_clear(self):
        # for i in range(self.ui.lst_item_list.count()):
        #     item = self.ui.item_list.item(i)
        #     widget = self.ui.lst_item_list.itemWidget(item)
        #     if widget is not None:
        #         self.db.set_visible_product(widget.id, False)
        self.ui.lst_item_list.clear()
        self.item_dict.clear()

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
        item_count = 0
        for i, item in enumerate(items):
            if not os.path.exists(item):
                continue

            if os.path.isfile(item):
                add = self._add_item(item)
                if add:
                    item_count += 1

            if os.path.isdir(item):
                for f in os.listdir(item):
                    if os.path.isdir(f):
                        continue
                    add = self._add_item(os.path.join(item, f))
                    if add:
                        item_count += 1
        if item_count == 0:
            self.ui.statusbar.showMessage("No items have been added.")

    def _check_exist_item(self, file_path) -> bool:
        if file_path in self.item_dict:
            return True
        return False

    def _add_item(self, file_path: str) -> bool:
        if not self._check_file_type(file_path) or self._check_exist_item(file_path):
            return False

        widget = UpscaleItem(self, file_path)

        title_item = QListWidgetItem(self.ui.lst_item_list)
        self.item_dict[file_path] = title_item
        title_item.setSizeHint(widget.sizeHint())
        self.ui.lst_item_list.addItem(title_item)
        self.ui.lst_item_list.setItemWidget(title_item, widget)

        return True

    def closeEvent(self, event):
        self.itemState.stop()
