from datetime import datetime
from enum import Enum

from PySide6.QtCore import Qt
from PySide6 import QtCore, QtGui
from PySide6.QtCore import QTime, QTimer, QDate
from PySide6.QtWidgets import QListWidgetItem, QMainWindow
from constant.SettingEnum import SettingEnum

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


    def _init_connect(self):
        self.ui.cmb_format.activated.connect(self._save_config)
        self.ui.cmb_tile_size.activated.connect(self._save_config)
        self.ui.chb_tta_mode.stateChanged.connect(self._save_config)
        self.ui.cmb_upscale_ratio.activated.connect(self._save_config)
        self.ui.cmb_model_name.activated.connect(self._save_config)
        self.ui.cmb_jpg_optimize.activated.connect(self._save_config)
        # self.ui.cmb_scale_ratio.currentTextChanged.connect(self.on_)
        # self.ui.btnStart.clicked.connect(self.on_click_start)
    
    def _save_config(self):
        self.config.setting[SettingEnum.FORMAT] = self.ui.cmb_format.currentText()
        self.config.setting[SettingEnum.TILE_SIZE] = self.ui.cmb_tile_size.currentText()
        self.config.setting[SettingEnum.TTA_MODE] = True if self.ui.chb_tta_mode.checkState() == Qt.CheckState.Checked else False
        self.config.setting[SettingEnum.UPSCALE_RATIO] = self.ui.cmb_upscale_ratio.currentText()
        self.config.setting[SettingEnum.MODEL_NAME] = self.ui.cmb_model_name.currentText()
        self.config.setting[SettingEnum.JPG_OPTIMIZE] = self.ui.cmb_jpg_optimize.currentText()
        self.config.save()
    
    def _load_config(self):
        self.ui.cmb_format.setCurrentText(self.config.setting[SettingEnum.FORMAT])
        self.ui.cmb_tile_size.setCurrentText(self.config.setting[SettingEnum.TILE_SIZE])
        self.ui.chb_tta_mode.setCheckState(
            Qt.CheckState.Checked if self.config.setting[SettingEnum.TTA_MODE] == True else Qt.CheckState.Unchecked
        )
        self.ui.cmb_upscale_ratio.setCurrentText(self.config.setting[SettingEnum.UPSCALE_RATIO])
        self.ui.cmb_model_name.setCurrentText(self.config.setting[SettingEnum.MODEL_NAME])
        self.ui.cmb_jpg_optimize.setCurrentText(self.config.setting[SettingEnum.JPG_OPTIMIZE])


    def on_click_start(self):
        self.save_config()

