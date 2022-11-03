from enum import Enum
import os
from tkinter import Widget

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import QObject, Qt, Signal, Slot
from PySide6.QtGui import QDragEnterEvent, QDragMoveEvent, QDropEvent
from PySide6.QtWidgets import QListWidgetItem, QMainWindow

import MainWindow
from constant.SettingEnum import SettingEnum
from ItemStateWorker import ItemStateWorker
from lib.QToaster import QToaster
from ui.ui_MainWindow import Ui_MainWindow
from UpscaleItem import ItemState, UpscaleItem
from util.Config import Config
from util.message import toast


class MainState(Enum):
    START = 0
    STOP = 1


class MainWindowSignal(QObject):
    item_remove = Signal(str, str)  # id, file_path
    item_state_change = Signal(str, str, ItemState)  # id, file_path, Item state


class MainWindow(QMainWindow):
    signals = MainWindowSignal()

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

        self.state = MainState.STOP

    def _init_connect(self):
        #### signal
        self.signals.item_remove.connect(self._on_item_remove)
        self.signals.item_state_change.connect(self._on_item_state_change)

        #### config
        self.ui.cmb_format.activated.connect(self._save_config)
        self.ui.cmb_tile_size.activated.connect(self._save_config)
        self.ui.chb_tta_mode.stateChanged.connect(self._save_config)
        self.ui.chb_replace_origin.stateChanged.connect(self._save_config)
        self.ui.cmb_upscale_ratio.activated.connect(self._save_config)
        self.ui.cmb_model_name.activated.connect(self._save_config)
        self.ui.cmb_jpg_optimize.activated.connect(self._save_config)

        ### List
        self.ui.lst_item_list.setDragEnabled(True)
        self.ui.lst_item_list.setAcceptDrops(True)
        self.ui.lst_item_list.dragEnterEvent = self._on_list_drag_enter
        self.ui.lst_item_list.dragMoveEvent = self._on_list_drag_move
        self.ui.lst_item_list.dropEvent = self._on_list_drop
        self.ui.lst_item_list.setDragDropMode(
            QtWidgets.QAbstractItemView.DragDropMode.InternalMove
        )

        # buttons
        self.ui.btn_start.clicked.connect(self._on_click_start)
        self.ui.btn_start.setStyleSheet("background-color: #5CB8FF")
        self.ui.btn_list_clear.clicked.connect(self._on_click_list_clear)
        self.ui.btn_done_clear.clicked.connect(self._on_done_clear)
        self.ui.btn_add_file.clicked.connect(self._on_click_add_file)
        self.ui.btn_add_folder.clicked.connect(self._on_click_add_folder)

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
        if self.state == MainState.START:
            toast(self, self.tr("Already started"))
            return
        toast(self, self.tr("Start"))
        self.state = MainState.START
        res = self.start_next()
        if res == False:
            toast(self, self.tr("nothing."))

    def _on_click_list_clear(self):
        if self.state == MainState.START:
            toast(self, self.tr("Wait end."))
            return

        self.ui.lst_item_list.clear()
        self.item_dict.clear()

    def _on_list_drag_enter(self, event: QDragEnterEvent):
        # event.accept()
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def _on_list_drag_move(self, event: QDragMoveEvent):
        # event.accept()
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
                continue

            if os.path.isdir(item):
                for f in os.listdir(item):
                    if os.path.isdir(f):
                        continue
                    add = self._add_item(os.path.join(item, f))
                    if add:
                        item_count += 1

        if item_count == 0:
            msg = self.tr("No items have been added.")
            self.ui.statusbar.showMessage(msg)
            toast(self, msg)

    def _check_exist_item(self, file_path) -> bool:
        if file_path in self.item_dict:
            return True
        return False

    def item_count(self):
        return self.ui.lst_item_list.count()

    def get_item(self, file_path: str):
        return self.item_dict[file_path]

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

    @Slot(str, str)
    def _on_item_remove(self, id: str, file_path: str):
        self._remove_item(file_path)

    @Slot(str, str, ItemState)
    def _on_item_state_change(self, id: str, file_path: str, state: ItemState):
        if state == ItemState.DONE:
            """
            완료 되면
            """
            if self.state == MainState.START:
                if self.start_next() == False:
                    self.set_all_start_btn_enable(True)
                    self.state = MainState.STOP

    def _find_next_item(self):
        for i in range(self.ui.lst_item_list.count()):
            item = self.ui.lst_item_list.item(i)
            widget = self.ui.lst_item_list.itemWidget(item)
            if widget is not None:
                if widget.state == ItemState.READY:
                    return widget

    def _on_done_clear(self):
        for i in reversed(range(self.ui.lst_item_list.count())):
            item = self.ui.lst_item_list.item(i)
            widget = self.ui.lst_item_list.itemWidget(item)
            if widget is not None:
                if widget.state == ItemState.DONE:
                    self._remove_item(widget.file_path)

    def _get_widget(self, file_path: str) -> Widget:
        for i in range(self.ui.lst_item_list.count()):
            item = self.ui.lst_item_list.item(i)
            widget = self.ui.lst_item_list.itemWidget(item)
            if widget is not None and widget.file_path == file_path:
                return widget
        return None

    def _remove_item(self, file_name: str):
        item = self.item_dict[file_name]
        if item is None:
            return
        self.ui.lst_item_list.takeItem(self.ui.lst_item_list.row(item))
        del self.item_dict[file_name]

    def check_doing_item(self) -> bool:
        for i in range(self.ui.lst_item_list.count()):
            item = self.ui.lst_item_list.item(i)
            widget: UpscaleItem = self.ui.lst_item_list.itemWidget(item)
            if widget:
                if widget.state == ItemState.DOING:
                    return True
        return False

    def set_all_start_btn_enable(self, value):
        for i in range(self.ui.lst_item_list.count()):
            item = self.ui.lst_item_list.item(i)
            widget: UpscaleItem = self.ui.lst_item_list.itemWidget(item)
            if widget:
                widget.btn_start_enable(value)

    def start_next(self) -> bool:
        if self.state == MainState.STOP:
            return False
        if self.check_doing_item():
            return False
        for i in range(self.ui.lst_item_list.count()):
            item = self.ui.lst_item_list.item(i)
            upscaleItem: UpscaleItem = self.ui.lst_item_list.itemWidget(item)
            if upscaleItem:
                if upscaleItem.state == ItemState.READY:
                    upscaleItem.on_click_run()
                    return True
        return False
    


    def _on_click_add_folder(self):
        file = str(QtWidgets.QFileDialog.getExistingDirectory(self, self.tr("Select Directory")))
        if file:
            self._add_items([file])

    def _on_click_add_file(self):
        fileNames = QtWidgets.QFileDialog.getOpenFileNames(self, self.tr("Select Directory"))
        if len(fileNames[0]) == 0:
            return
        files = []
        for f in fileNames[0]:
            files.append(str(f))
        
        self._add_items(files)
