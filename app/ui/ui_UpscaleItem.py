# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UpscaleItem.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_UpscaleItem(object):
    def setupUi(self, UpscaleItem):
        if not UpscaleItem.objectName():
            UpscaleItem.setObjectName(u"UpscaleItem")
        UpscaleItem.resize(635, 78)
        UpscaleItem.setMaximumSize(QSize(16777215, 78))
        self.horizontalLayout_2 = QHBoxLayout(UpscaleItem)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_file_name = QLabel(UpscaleItem)
        self.lbl_file_name.setObjectName(u"lbl_file_name")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_file_name.sizePolicy().hasHeightForWidth())
        self.lbl_file_name.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lbl_file_name.setFont(font)
        self.lbl_file_name.setTextFormat(Qt.PlainText)
        self.lbl_file_name.setScaledContents(True)

        self.horizontalLayout.addWidget(self.lbl_file_name)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_open_folder = QPushButton(UpscaleItem)
        self.btn_open_folder.setObjectName(u"btn_open_folder")
        icon = QIcon()
        icon.addFile(u":/icon/icons/folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_open_folder.setIcon(icon)
        self.btn_open_folder.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_open_folder)

        self.btn_delete = QPushButton(UpscaleItem)
        self.btn_delete.setObjectName(u"btn_delete")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/trash-delete-bin.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete.setIcon(icon1)
        self.btn_delete.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_delete)

        self.horizontalLayout.setStretch(0, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_path = QLabel(UpscaleItem)
        self.lbl_path.setObjectName(u"lbl_path")
        sizePolicy.setHeightForWidth(self.lbl_path.sizePolicy().hasHeightForWidth())
        self.lbl_path.setSizePolicy(sizePolicy)
        self.lbl_path.setTextFormat(Qt.PlainText)
        self.lbl_path.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.lbl_path)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.lbl_state = QLabel(UpscaleItem)
        self.lbl_state.setObjectName(u"lbl_state")

        self.horizontalLayout_3.addWidget(self.lbl_state)

        self.pgb_progress = QProgressBar(UpscaleItem)
        self.pgb_progress.setObjectName(u"pgb_progress")
        self.pgb_progress.setMaximumSize(QSize(150, 16777215))
        self.pgb_progress.setValue(24)

        self.horizontalLayout_3.addWidget(self.pgb_progress)

        self.horizontalLayout_3.setStretch(0, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(UpscaleItem)

        QMetaObject.connectSlotsByName(UpscaleItem)
    # setupUi

    def retranslateUi(self, UpscaleItem):
        UpscaleItem.setWindowTitle(QCoreApplication.translate("UpscaleItem", u"Form", None))
        self.lbl_file_name.setText(QCoreApplication.translate("UpscaleItem", u"lbl_file_name", None))
        self.btn_open_folder.setText("")
        self.btn_delete.setText("")
        self.lbl_path.setText(QCoreApplication.translate("UpscaleItem", u"lbl_path", None))
        self.lbl_state.setText(QCoreApplication.translate("UpscaleItem", u"lbl_state", None))
    # retranslateUi

