# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Item.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(779, 78)
        Form.setMaximumSize(QSize(16777215, 78))
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_file_name = QLabel(Form)
        self.lbl_file_name.setObjectName(u"lbl_file_name")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.lbl_file_name.setFont(font)

        self.horizontalLayout.addWidget(self.lbl_file_name)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_open_folder = QPushButton(Form)
        self.btn_open_folder.setObjectName(u"btn_open_folder")
        icon = QIcon()
        icon.addFile(u":/icon/icons/folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_open_folder.setIcon(icon)
        self.btn_open_folder.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_open_folder)

        self.btn_delete = QPushButton(Form)
        self.btn_delete.setObjectName(u"btn_delete")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/trash-delete-bin.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete.setIcon(icon1)
        self.btn_delete.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_delete)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_state = QLabel(Form)
        self.lbl_state.setObjectName(u"lbl_state")

        self.horizontalLayout_3.addWidget(self.lbl_state)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximumSize(QSize(150, 16777215))
        self.progressBar.setValue(24)

        self.horizontalLayout_3.addWidget(self.progressBar)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_file_name.setText(QCoreApplication.translate("Form", u"lbl_file_name", None))
        self.btn_open_folder.setText("")
        self.btn_delete.setText("")
        self.lbl_state.setText(QCoreApplication.translate("Form", u"lbl_state", None))
    # retranslateUi

