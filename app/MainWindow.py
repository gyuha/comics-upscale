from datetime import datetime
from enum import Enum

import PySide6.QtCore
from PySide6 import QtCore, QtGui
from PySide6.QtCore import QTime, QTimer, QDate
from PySide6.QtWidgets import QListWidgetItem, QMainWindow

from lib.Config import Config
from ui.ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.config = Config()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.__init_connect()


    def __init_connect(self):
        pass
        # self.ui.btnStart.clicked.connect(self.on_click_start)

    def save_config(self):
        pass
        # self.config.setting["id"] = self.ui.leID.text().strip()
        # self.config.setting["password"] = Crypto.encrypt(
        #     self.ui.lePassword.text().strip()
        # )

        # self.config.setting["reserve_date"] = self.ui.deReserveDate.dateTime().toString(
        #     "yyyy-MM-dd"
        # )
        # self.config.setting["start_time"] = self.ui.teStartTime.time().toString("hh:mm")
        # self.config.setting["end_time"] = self.ui.teEndTime.time().toString("hh:mm")
        # self.config.setting["retry_count"] = int(self.ui.leRetryCount.text())
        # self.config.setting["run_duration"] = int(self.ui.leRunDuration.text())
        # self.config.save()

    def on_click_start(self):
        self.save_config()
        self.driver = get_driver()
        self.login()

