# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(784, 636)
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
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout_2.setHorizontalSpacing(10)
        self.formLayout_2.setVerticalSpacing(10)
        self.formLayout_2.setContentsMargins(-1, -1, 5, -1)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.cb_format = QComboBox(self.centralwidget)
        self.cb_format.setObjectName(u"cb_format")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.cb_format)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.cb_scale_ratio = QComboBox(self.centralwidget)
        self.cb_scale_ratio.setObjectName(u"cb_scale_ratio")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.cb_scale_ratio)


        self.horizontalLayout.addLayout(self.formLayout_2)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout_3.setHorizontalSpacing(10)
        self.formLayout_3.setVerticalSpacing(10)
        self.formLayout_3.setContentsMargins(-1, -1, 5, -1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.cb_tile_size = QComboBox(self.centralwidget)
        self.cb_tile_size.setObjectName(u"cb_tile_size")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.cb_tile_size)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.cb_model_name = QComboBox(self.centralwidget)
        self.cb_model_name.setObjectName(u"cb_model_name")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.cb_model_name)


        self.horizontalLayout.addLayout(self.formLayout_3)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(10)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.checkBox)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.cb_jpg_optimize = QCheckBox(self.centralwidget)
        self.cb_jpg_optimize.setObjectName(u"cb_jpg_optimize")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.cb_jpg_optimize)


        self.horizontalLayout.addLayout(self.formLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setDragEnabled(False)

        self.verticalLayout_2.addWidget(self.listWidget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btn_start = QPushButton(self.centralwidget)
        self.btn_start.setObjectName(u"btn_start")

        self.horizontalLayout_3.addWidget(self.btn_start)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalLayout_2.setStretch(1, 1)

        self.verticalLayout.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Comics upscale", None))
        self.action_always_top.setText(QCoreApplication.translate("MainWindow", u"\ud56d\uc0c1\uc704", None))
        self.action_clipboard_toggle.setText(QCoreApplication.translate("MainWindow", u"\ud074\ub9bd\ubcf4\ub4dc\uc5d0\uc11c \ucd94\uac00", None))
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"\uc885\ub8cc(&q)", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Format", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Scale ratio", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Tile size", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Model name", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TTA Mode", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"TTA mode", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Jpg optimize", None))
        self.cb_jpg_optimize.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Add folder", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Add file", None))
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
    # retranslateUi

