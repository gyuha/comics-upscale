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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFormLayout, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 472)
        MainWindow.setMinimumSize(QSize(800, 0))
        icon = QIcon()
        icon.addFile(u":/icon/icons/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
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
        self.formLayout_2.setContentsMargins(10, -1, 5, -1)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.cmb_format = QComboBox(self.centralwidget)
        self.cmb_format.addItem("")
        self.cmb_format.addItem("")
        self.cmb_format.addItem("")
        self.cmb_format.setObjectName(u"cmb_format")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.cmb_format)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.cmb_upscale_ratio = QComboBox(self.centralwidget)
        self.cmb_upscale_ratio.addItem("")
        self.cmb_upscale_ratio.addItem("")
        self.cmb_upscale_ratio.addItem("")
        self.cmb_upscale_ratio.setObjectName(u"cmb_upscale_ratio")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.cmb_upscale_ratio)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.cmb_jpg_optimize = QComboBox(self.centralwidget)
        self.cmb_jpg_optimize.addItem("")
        self.cmb_jpg_optimize.addItem("")
        self.cmb_jpg_optimize.addItem("")
        self.cmb_jpg_optimize.addItem("")
        self.cmb_jpg_optimize.addItem("")
        self.cmb_jpg_optimize.addItem("")
        self.cmb_jpg_optimize.addItem("")
        self.cmb_jpg_optimize.addItem("")
        self.cmb_jpg_optimize.addItem("")
        self.cmb_jpg_optimize.addItem("")
        self.cmb_jpg_optimize.addItem("")
        self.cmb_jpg_optimize.addItem("")
        self.cmb_jpg_optimize.addItem("")
        self.cmb_jpg_optimize.addItem("")
        self.cmb_jpg_optimize.addItem("")
        self.cmb_jpg_optimize.addItem("")
        self.cmb_jpg_optimize.addItem("")
        self.cmb_jpg_optimize.addItem("")
        self.cmb_jpg_optimize.addItem("")
        self.cmb_jpg_optimize.addItem("")
        self.cmb_jpg_optimize.addItem("")
        self.cmb_jpg_optimize.addItem("")
        self.cmb_jpg_optimize.addItem("")
        self.cmb_jpg_optimize.addItem("")
        self.cmb_jpg_optimize.addItem("")
        self.cmb_jpg_optimize.addItem("")
        self.cmb_jpg_optimize.setObjectName(u"cmb_jpg_optimize")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.cmb_jpg_optimize)


        self.horizontalLayout.addLayout(self.formLayout_2)

        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setContentsMargins(10, -1, -1, -1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.cmb_tile_size = QComboBox(self.centralwidget)
        self.cmb_tile_size.addItem("")
        self.cmb_tile_size.addItem("")
        self.cmb_tile_size.addItem("")
        self.cmb_tile_size.addItem("")
        self.cmb_tile_size.addItem("")
        self.cmb_tile_size.addItem("")
        self.cmb_tile_size.addItem("")
        self.cmb_tile_size.addItem("")
        self.cmb_tile_size.addItem("")
        self.cmb_tile_size.addItem("")
        self.cmb_tile_size.addItem("")
        self.cmb_tile_size.addItem("")
        self.cmb_tile_size.addItem("")
        self.cmb_tile_size.addItem("")
        self.cmb_tile_size.addItem("")
        self.cmb_tile_size.addItem("")
        self.cmb_tile_size.addItem("")
        self.cmb_tile_size.addItem("")
        self.cmb_tile_size.addItem("")
        self.cmb_tile_size.addItem("")
        self.cmb_tile_size.addItem("")
        self.cmb_tile_size.addItem("")
        self.cmb_tile_size.addItem("")
        self.cmb_tile_size.addItem("")
        self.cmb_tile_size.addItem("")
        self.cmb_tile_size.addItem("")
        self.cmb_tile_size.addItem("")
        self.cmb_tile_size.addItem("")
        self.cmb_tile_size.addItem("")
        self.cmb_tile_size.addItem("")
        self.cmb_tile_size.addItem("")
        self.cmb_tile_size.addItem("")
        self.cmb_tile_size.addItem("")
        self.cmb_tile_size.setObjectName(u"cmb_tile_size")

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.cmb_tile_size)

        self.cmb_model_name = QComboBox(self.centralwidget)
        self.cmb_model_name.addItem("")
        self.cmb_model_name.addItem("")
        self.cmb_model_name.addItem("")
        self.cmb_model_name.setObjectName(u"cmb_model_name")

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.cmb_model_name)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_5)


        self.horizontalLayout.addLayout(self.formLayout_5)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setContentsMargins(10, -1, -1, -1)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.chb_tta_mode = QCheckBox(self.centralwidget)
        self.chb_tta_mode.setObjectName(u"chb_tta_mode")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.chb_tta_mode)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_7)

        self.chb_replace_origin = QCheckBox(self.centralwidget)
        self.chb_replace_origin.setObjectName(u"chb_replace_origin")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.chb_replace_origin)


        self.horizontalLayout.addLayout(self.formLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.lst_item_list = QListWidget(self.centralwidget)
        self.lst_item_list.setObjectName(u"lst_item_list")
        self.lst_item_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.lst_item_list.setDragEnabled(True)
        self.lst_item_list.setDragDropMode(QAbstractItemView.InternalMove)
        self.lst_item_list.setDefaultDropAction(Qt.MoveAction)

        self.verticalLayout_2.addWidget(self.lst_item_list)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.btn_add_folder = QPushButton(self.centralwidget)
        self.btn_add_folder.setObjectName(u"btn_add_folder")

        self.horizontalLayout_3.addWidget(self.btn_add_folder)

        self.btn_add_file = QPushButton(self.centralwidget)
        self.btn_add_file.setObjectName(u"btn_add_file")

        self.horizontalLayout_3.addWidget(self.btn_add_file)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.lbl_state = QLabel(self.centralwidget)
        self.lbl_state.setObjectName(u"lbl_state")

        self.horizontalLayout_3.addWidget(self.lbl_state)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.pgb_state = QProgressBar(self.centralwidget)
        self.pgb_state.setObjectName(u"pgb_state")
        self.pgb_state.setValue(24)

        self.horizontalLayout_3.addWidget(self.pgb_state)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.btn_list_clear = QPushButton(self.centralwidget)
        self.btn_list_clear.setObjectName(u"btn_list_clear")

        self.horizontalLayout_3.addWidget(self.btn_list_clear)

        self.btn_done_clear = QPushButton(self.centralwidget)
        self.btn_done_clear.setObjectName(u"btn_done_clear")

        self.horizontalLayout_3.addWidget(self.btn_done_clear)

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
        self.cmb_format.setItemText(0, QCoreApplication.translate("MainWindow", u"jpg", None))
        self.cmb_format.setItemText(1, QCoreApplication.translate("MainWindow", u"png", None))
        self.cmb_format.setItemText(2, QCoreApplication.translate("MainWindow", u"webp", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Upscale ratio", None))
        self.cmb_upscale_ratio.setItemText(0, QCoreApplication.translate("MainWindow", u"2", None))
        self.cmb_upscale_ratio.setItemText(1, QCoreApplication.translate("MainWindow", u"3", None))
        self.cmb_upscale_ratio.setItemText(2, QCoreApplication.translate("MainWindow", u"4", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Jpg optimize", None))
        self.cmb_jpg_optimize.setItemText(0, QCoreApplication.translate("MainWindow", u"100 (OFF)", None))
        self.cmb_jpg_optimize.setItemText(1, QCoreApplication.translate("MainWindow", u"99", None))
        self.cmb_jpg_optimize.setItemText(2, QCoreApplication.translate("MainWindow", u"98", None))
        self.cmb_jpg_optimize.setItemText(3, QCoreApplication.translate("MainWindow", u"97", None))
        self.cmb_jpg_optimize.setItemText(4, QCoreApplication.translate("MainWindow", u"96", None))
        self.cmb_jpg_optimize.setItemText(5, QCoreApplication.translate("MainWindow", u"95", None))
        self.cmb_jpg_optimize.setItemText(6, QCoreApplication.translate("MainWindow", u"94", None))
        self.cmb_jpg_optimize.setItemText(7, QCoreApplication.translate("MainWindow", u"93", None))
        self.cmb_jpg_optimize.setItemText(8, QCoreApplication.translate("MainWindow", u"92", None))
        self.cmb_jpg_optimize.setItemText(9, QCoreApplication.translate("MainWindow", u"91", None))
        self.cmb_jpg_optimize.setItemText(10, QCoreApplication.translate("MainWindow", u"90", None))
        self.cmb_jpg_optimize.setItemText(11, QCoreApplication.translate("MainWindow", u"89", None))
        self.cmb_jpg_optimize.setItemText(12, QCoreApplication.translate("MainWindow", u"88", None))
        self.cmb_jpg_optimize.setItemText(13, QCoreApplication.translate("MainWindow", u"87", None))
        self.cmb_jpg_optimize.setItemText(14, QCoreApplication.translate("MainWindow", u"86", None))
        self.cmb_jpg_optimize.setItemText(15, QCoreApplication.translate("MainWindow", u"85", None))
        self.cmb_jpg_optimize.setItemText(16, QCoreApplication.translate("MainWindow", u"84", None))
        self.cmb_jpg_optimize.setItemText(17, QCoreApplication.translate("MainWindow", u"83", None))
        self.cmb_jpg_optimize.setItemText(18, QCoreApplication.translate("MainWindow", u"82", None))
        self.cmb_jpg_optimize.setItemText(19, QCoreApplication.translate("MainWindow", u"81", None))
        self.cmb_jpg_optimize.setItemText(20, QCoreApplication.translate("MainWindow", u"80", None))
        self.cmb_jpg_optimize.setItemText(21, QCoreApplication.translate("MainWindow", u"79", None))
        self.cmb_jpg_optimize.setItemText(22, QCoreApplication.translate("MainWindow", u"78", None))
        self.cmb_jpg_optimize.setItemText(23, QCoreApplication.translate("MainWindow", u"77", None))
        self.cmb_jpg_optimize.setItemText(24, QCoreApplication.translate("MainWindow", u"76", None))
        self.cmb_jpg_optimize.setItemText(25, QCoreApplication.translate("MainWindow", u"75", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Tile size", None))
        self.cmb_tile_size.setItemText(0, QCoreApplication.translate("MainWindow", u"0 (Auto)", None))
        self.cmb_tile_size.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.cmb_tile_size.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.cmb_tile_size.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.cmb_tile_size.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.cmb_tile_size.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.cmb_tile_size.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))
        self.cmb_tile_size.setItemText(7, QCoreApplication.translate("MainWindow", u"7", None))
        self.cmb_tile_size.setItemText(8, QCoreApplication.translate("MainWindow", u"8", None))
        self.cmb_tile_size.setItemText(9, QCoreApplication.translate("MainWindow", u"9", None))
        self.cmb_tile_size.setItemText(10, QCoreApplication.translate("MainWindow", u"10", None))
        self.cmb_tile_size.setItemText(11, QCoreApplication.translate("MainWindow", u"11", None))
        self.cmb_tile_size.setItemText(12, QCoreApplication.translate("MainWindow", u"12", None))
        self.cmb_tile_size.setItemText(13, QCoreApplication.translate("MainWindow", u"13", None))
        self.cmb_tile_size.setItemText(14, QCoreApplication.translate("MainWindow", u"14", None))
        self.cmb_tile_size.setItemText(15, QCoreApplication.translate("MainWindow", u"15", None))
        self.cmb_tile_size.setItemText(16, QCoreApplication.translate("MainWindow", u"16", None))
        self.cmb_tile_size.setItemText(17, QCoreApplication.translate("MainWindow", u"17", None))
        self.cmb_tile_size.setItemText(18, QCoreApplication.translate("MainWindow", u"18", None))
        self.cmb_tile_size.setItemText(19, QCoreApplication.translate("MainWindow", u"19", None))
        self.cmb_tile_size.setItemText(20, QCoreApplication.translate("MainWindow", u"20", None))
        self.cmb_tile_size.setItemText(21, QCoreApplication.translate("MainWindow", u"21", None))
        self.cmb_tile_size.setItemText(22, QCoreApplication.translate("MainWindow", u"22", None))
        self.cmb_tile_size.setItemText(23, QCoreApplication.translate("MainWindow", u"23", None))
        self.cmb_tile_size.setItemText(24, QCoreApplication.translate("MainWindow", u"24", None))
        self.cmb_tile_size.setItemText(25, QCoreApplication.translate("MainWindow", u"25", None))
        self.cmb_tile_size.setItemText(26, QCoreApplication.translate("MainWindow", u"26", None))
        self.cmb_tile_size.setItemText(27, QCoreApplication.translate("MainWindow", u"27", None))
        self.cmb_tile_size.setItemText(28, QCoreApplication.translate("MainWindow", u"28", None))
        self.cmb_tile_size.setItemText(29, QCoreApplication.translate("MainWindow", u"29", None))
        self.cmb_tile_size.setItemText(30, QCoreApplication.translate("MainWindow", u"30", None))
        self.cmb_tile_size.setItemText(31, QCoreApplication.translate("MainWindow", u"31", None))
        self.cmb_tile_size.setItemText(32, QCoreApplication.translate("MainWindow", u"32", None))

        self.cmb_model_name.setItemText(0, QCoreApplication.translate("MainWindow", u"realesr-animevideov3", None))
        self.cmb_model_name.setItemText(1, QCoreApplication.translate("MainWindow", u"realesrgan-x4plus", None))
        self.cmb_model_name.setItemText(2, QCoreApplication.translate("MainWindow", u"realesrgan-x4plus-anime", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Model name", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TTA Mode", None))
        self.chb_tta_mode.setText(QCoreApplication.translate("MainWindow", u"TTA mode", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Replace origin", None))
        self.chb_replace_origin.setText(QCoreApplication.translate("MainWindow", u"Replace origin", None))
        self.btn_add_folder.setText(QCoreApplication.translate("MainWindow", u"Add folder", None))
        self.btn_add_file.setText(QCoreApplication.translate("MainWindow", u"Add file", None))
        self.lbl_state.setText(QCoreApplication.translate("MainWindow", u"0/0", None))
        self.btn_list_clear.setText(QCoreApplication.translate("MainWindow", u"List clear", None))
        self.btn_done_clear.setText(QCoreApplication.translate("MainWindow", u"Done Clear", None))
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
    # retranslateUi

