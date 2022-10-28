# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QStatusBar, QTimeEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(629, 664)
        self.action_always_top = QAction(MainWindow)
        self.action_always_top.setObjectName(u"action_always_top")
        self.action_always_top.setCheckable(True)
        self.action_clipboard_toggle = QAction(MainWindow)
        self.action_clipboard_toggle.setObjectName(u"action_clipboard_toggle")
        self.action_clipboard_toggle.setCheckable(True)
        self.action_clipboard_toggle.setChecked(True)
        self.action_exit = QAction(MainWindow)
        self.action_exit.setObjectName(u"action_exit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget.setAutoFillBackground(False)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 6, 2, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.teEndTime = QTimeEdit(self.centralwidget)
        self.teEndTime.setObjectName(u"teEndTime")

        self.gridLayout.addWidget(self.teEndTime, 6, 3, 1, 1)

        self.leRunDuration = QLineEdit(self.centralwidget)
        self.leRunDuration.setObjectName(u"leRunDuration")

        self.gridLayout.addWidget(self.leRunDuration, 7, 1, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)

        self.lePassword = QLineEdit(self.centralwidget)
        self.lePassword.setObjectName(u"lePassword")
        self.lePassword.setMaximumSize(QSize(16777215, 16777215))
        self.lePassword.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.lePassword, 1, 3, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 3, 0, 1, 4)

        self.teStartTime = QTimeEdit(self.centralwidget)
        self.teStartTime.setObjectName(u"teStartTime")

        self.gridLayout.addWidget(self.teStartTime, 6, 1, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 2)

        self.deReserveDate = QDateEdit(self.centralwidget)
        self.deReserveDate.setObjectName(u"deReserveDate")

        self.gridLayout.addWidget(self.deReserveDate, 5, 1, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 7, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 2)

        self.btnStart = QPushButton(self.centralwidget)
        self.btnStart.setObjectName(u"btnStart")

        self.gridLayout.addWidget(self.btnStart, 9, 0, 1, 4)

        self.leID = QLineEdit(self.centralwidget)
        self.leID.setObjectName(u"leID")
        self.leID.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.leID, 1, 1, 1, 1)

        self.teLog = QPlainTextEdit(self.centralwidget)
        self.teLog.setObjectName(u"teLog")
        self.teLog.setMinimumSize(QSize(0, 300))

        self.gridLayout.addWidget(self.teLog, 8, 0, 1, 4)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 7, 2, 1, 1)

        self.leRetryCount = QLineEdit(self.centralwidget)
        self.leRetryCount.setObjectName(u"leRetryCount")

        self.gridLayout.addWidget(self.leRetryCount, 7, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Namyeoju", None))
        self.action_always_top.setText(QCoreApplication.translate("MainWindow", u"\ud56d\uc0c1\uc704", None))
        self.action_clipboard_toggle.setText(QCoreApplication.translate("MainWindow", u"\ud074\ub9bd\ubcf4\ub4dc\uc5d0\uc11c \ucd94\uac00", None))
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"\uc885\ub8cc(&q)", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\ub05d \uc2dc\uac04", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\uc544\uc774\ub514", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\uc608\uc57d \ub0a0\uc9dc", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uc791 \uc2dc\uac04", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\uacc4\uc815", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\uc2e4\ud589 \uac04\uaca9", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\uc554\ud638", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\uc608\uc57d", None))
        self.btnStart.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uc791", None))
        self.teLog.setPlainText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\uc7ac\uc2dc\ub3c4 \ud69f\uc218", None))
    # retranslateUi

