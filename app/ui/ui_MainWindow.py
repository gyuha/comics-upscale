/********************************************************************************
** Form generated from reading UI file 'MainWindow.ui'
**
** Created by: Qt User Interface Compiler version 6.4.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QFormLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *action_always_top;
    QAction *action_clipboard_toggle;
    QAction *action_exit;
    QWidget *centralwidget;
    QVBoxLayout *verticalLayout;
    QVBoxLayout *verticalLayout_2;
    QHBoxLayout *horizontalLayout;
    QFormLayout *formLayout_2;
    QLabel *label;
    QComboBox *cb_format;
    QLabel *label_4;
    QComboBox *cb_scale_ratio;
    QFormLayout *formLayout_3;
    QLabel *label_2;
    QComboBox *cb_tile_size;
    QLabel *label_5;
    QComboBox *cb_model_name;
    QFormLayout *formLayout;
    QLabel *label_3;
    QCheckBox *checkBox;
    QLabel *label_6;
    QComboBox *cb_jpg_optimize;
    QListWidget *listWidget;
    QHBoxLayout *horizontalLayout_3;
    QPushButton *pushButton_2;
    QPushButton *pushButton_3;
    QSpacerItem *horizontalSpacer;
    QPushButton *btn_start;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName("MainWindow");
        MainWindow->resize(784, 636);
        action_always_top = new QAction(MainWindow);
        action_always_top->setObjectName("action_always_top");
        action_always_top->setCheckable(true);
        action_clipboard_toggle = new QAction(MainWindow);
        action_clipboard_toggle->setObjectName("action_clipboard_toggle");
        action_clipboard_toggle->setCheckable(true);
        action_clipboard_toggle->setChecked(true);
        action_exit = new QAction(MainWindow);
        action_exit->setObjectName("action_exit");
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName("centralwidget");
        centralwidget->setMaximumSize(QSize(16777215, 16777215));
        centralwidget->setAutoFillBackground(false);
        verticalLayout = new QVBoxLayout(centralwidget);
        verticalLayout->setSpacing(0);
        verticalLayout->setObjectName("verticalLayout");
        verticalLayout->setContentsMargins(0, 0, 0, 0);
        verticalLayout_2 = new QVBoxLayout();
        verticalLayout_2->setObjectName("verticalLayout_2");
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName("horizontalLayout");
        horizontalLayout->setContentsMargins(10, 10, 10, 10);
        formLayout_2 = new QFormLayout();
        formLayout_2->setObjectName("formLayout_2");
        formLayout_2->setLabelAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        formLayout_2->setHorizontalSpacing(10);
        formLayout_2->setVerticalSpacing(10);
        formLayout_2->setContentsMargins(-1, -1, 5, -1);
        label = new QLabel(centralwidget);
        label->setObjectName("label");

        formLayout_2->setWidget(0, QFormLayout::LabelRole, label);

        cb_format = new QComboBox(centralwidget);
        cb_format->addItem(QString());
        cb_format->addItem(QString());
        cb_format->addItem(QString());
        cb_format->setObjectName("cb_format");

        formLayout_2->setWidget(0, QFormLayout::FieldRole, cb_format);

        label_4 = new QLabel(centralwidget);
        label_4->setObjectName("label_4");

        formLayout_2->setWidget(1, QFormLayout::LabelRole, label_4);

        cb_scale_ratio = new QComboBox(centralwidget);
        cb_scale_ratio->addItem(QString());
        cb_scale_ratio->addItem(QString());
        cb_scale_ratio->addItem(QString());
        cb_scale_ratio->setObjectName("cb_scale_ratio");

        formLayout_2->setWidget(1, QFormLayout::FieldRole, cb_scale_ratio);


        horizontalLayout->addLayout(formLayout_2);

        formLayout_3 = new QFormLayout();
        formLayout_3->setObjectName("formLayout_3");
        formLayout_3->setLabelAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        formLayout_3->setHorizontalSpacing(10);
        formLayout_3->setVerticalSpacing(10);
        formLayout_3->setContentsMargins(-1, -1, 5, -1);
        label_2 = new QLabel(centralwidget);
        label_2->setObjectName("label_2");

        formLayout_3->setWidget(0, QFormLayout::LabelRole, label_2);

        cb_tile_size = new QComboBox(centralwidget);
        cb_tile_size->addItem(QString());
        cb_tile_size->addItem(QString());
        cb_tile_size->addItem(QString());
        cb_tile_size->addItem(QString());
        cb_tile_size->addItem(QString());
        cb_tile_size->addItem(QString());
        cb_tile_size->addItem(QString());
        cb_tile_size->addItem(QString());
        cb_tile_size->addItem(QString());
        cb_tile_size->addItem(QString());
        cb_tile_size->addItem(QString());
        cb_tile_size->addItem(QString());
        cb_tile_size->addItem(QString());
        cb_tile_size->addItem(QString());
        cb_tile_size->addItem(QString());
        cb_tile_size->addItem(QString());
        cb_tile_size->addItem(QString());
        cb_tile_size->addItem(QString());
        cb_tile_size->addItem(QString());
        cb_tile_size->addItem(QString());
        cb_tile_size->addItem(QString());
        cb_tile_size->addItem(QString());
        cb_tile_size->addItem(QString());
        cb_tile_size->addItem(QString());
        cb_tile_size->addItem(QString());
        cb_tile_size->addItem(QString());
        cb_tile_size->addItem(QString());
        cb_tile_size->addItem(QString());
        cb_tile_size->addItem(QString());
        cb_tile_size->addItem(QString());
        cb_tile_size->addItem(QString());
        cb_tile_size->addItem(QString());
        cb_tile_size->addItem(QString());
        cb_tile_size->setObjectName("cb_tile_size");

        formLayout_3->setWidget(0, QFormLayout::FieldRole, cb_tile_size);

        label_5 = new QLabel(centralwidget);
        label_5->setObjectName("label_5");

        formLayout_3->setWidget(1, QFormLayout::LabelRole, label_5);

        cb_model_name = new QComboBox(centralwidget);
        cb_model_name->addItem(QString());
        cb_model_name->addItem(QString());
        cb_model_name->addItem(QString());
        cb_model_name->setObjectName("cb_model_name");

        formLayout_3->setWidget(1, QFormLayout::FieldRole, cb_model_name);


        horizontalLayout->addLayout(formLayout_3);

        formLayout = new QFormLayout();
        formLayout->setObjectName("formLayout");
        formLayout->setLabelAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        formLayout->setHorizontalSpacing(10);
        formLayout->setVerticalSpacing(10);
        label_3 = new QLabel(centralwidget);
        label_3->setObjectName("label_3");

        formLayout->setWidget(0, QFormLayout::LabelRole, label_3);

        checkBox = new QCheckBox(centralwidget);
        checkBox->setObjectName("checkBox");

        formLayout->setWidget(0, QFormLayout::FieldRole, checkBox);

        label_6 = new QLabel(centralwidget);
        label_6->setObjectName("label_6");

        formLayout->setWidget(1, QFormLayout::LabelRole, label_6);

        cb_jpg_optimize = new QComboBox(centralwidget);
        cb_jpg_optimize->addItem(QString());
        cb_jpg_optimize->addItem(QString());
        cb_jpg_optimize->addItem(QString());
        cb_jpg_optimize->addItem(QString());
        cb_jpg_optimize->addItem(QString());
        cb_jpg_optimize->addItem(QString());
        cb_jpg_optimize->addItem(QString());
        cb_jpg_optimize->addItem(QString());
        cb_jpg_optimize->addItem(QString());
        cb_jpg_optimize->addItem(QString());
        cb_jpg_optimize->addItem(QString());
        cb_jpg_optimize->addItem(QString());
        cb_jpg_optimize->addItem(QString());
        cb_jpg_optimize->addItem(QString());
        cb_jpg_optimize->addItem(QString());
        cb_jpg_optimize->addItem(QString());
        cb_jpg_optimize->addItem(QString());
        cb_jpg_optimize->addItem(QString());
        cb_jpg_optimize->addItem(QString());
        cb_jpg_optimize->addItem(QString());
        cb_jpg_optimize->addItem(QString());
        cb_jpg_optimize->addItem(QString());
        cb_jpg_optimize->addItem(QString());
        cb_jpg_optimize->addItem(QString());
        cb_jpg_optimize->addItem(QString());
        cb_jpg_optimize->addItem(QString());
        cb_jpg_optimize->setObjectName("cb_jpg_optimize");

        formLayout->setWidget(1, QFormLayout::FieldRole, cb_jpg_optimize);


        horizontalLayout->addLayout(formLayout);


        verticalLayout_2->addLayout(horizontalLayout);

        listWidget = new QListWidget(centralwidget);
        listWidget->setObjectName("listWidget");
        listWidget->setDragEnabled(false);

        verticalLayout_2->addWidget(listWidget);

        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setObjectName("horizontalLayout_3");
        horizontalLayout_3->setContentsMargins(10, 10, 10, 10);
        pushButton_2 = new QPushButton(centralwidget);
        pushButton_2->setObjectName("pushButton_2");

        horizontalLayout_3->addWidget(pushButton_2);

        pushButton_3 = new QPushButton(centralwidget);
        pushButton_3->setObjectName("pushButton_3");

        horizontalLayout_3->addWidget(pushButton_3);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_3->addItem(horizontalSpacer);

        btn_start = new QPushButton(centralwidget);
        btn_start->setObjectName("btn_start");

        horizontalLayout_3->addWidget(btn_start);


        verticalLayout_2->addLayout(horizontalLayout_3);

        verticalLayout_2->setStretch(1, 1);

        verticalLayout->addLayout(verticalLayout_2);

        MainWindow->setCentralWidget(centralwidget);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName("statusbar");
        MainWindow->setStatusBar(statusbar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "Comics upscale", nullptr));
        action_always_top->setText(QCoreApplication::translate("MainWindow", "\355\225\255\354\203\201\354\234\204", nullptr));
        action_clipboard_toggle->setText(QCoreApplication::translate("MainWindow", "\355\201\264\353\246\275\353\263\264\353\223\234\354\227\220\354\204\234 \354\266\224\352\260\200", nullptr));
        action_exit->setText(QCoreApplication::translate("MainWindow", "\354\242\205\353\243\214(&q)", nullptr));
        label->setText(QCoreApplication::translate("MainWindow", "Format", nullptr));
        cb_format->setItemText(0, QCoreApplication::translate("MainWindow", "jpg", nullptr));
        cb_format->setItemText(1, QCoreApplication::translate("MainWindow", "png", nullptr));
        cb_format->setItemText(2, QCoreApplication::translate("MainWindow", "webp", nullptr));

        label_4->setText(QCoreApplication::translate("MainWindow", "Scale ratio", nullptr));
        cb_scale_ratio->setItemText(0, QCoreApplication::translate("MainWindow", "2", nullptr));
        cb_scale_ratio->setItemText(1, QCoreApplication::translate("MainWindow", "3", nullptr));
        cb_scale_ratio->setItemText(2, QCoreApplication::translate("MainWindow", "4", nullptr));

        label_2->setText(QCoreApplication::translate("MainWindow", "Tile size", nullptr));
        cb_tile_size->setItemText(0, QCoreApplication::translate("MainWindow", "0 (Auto)", nullptr));
        cb_tile_size->setItemText(1, QCoreApplication::translate("MainWindow", "1", nullptr));
        cb_tile_size->setItemText(2, QCoreApplication::translate("MainWindow", "2", nullptr));
        cb_tile_size->setItemText(3, QCoreApplication::translate("MainWindow", "3", nullptr));
        cb_tile_size->setItemText(4, QCoreApplication::translate("MainWindow", "4", nullptr));
        cb_tile_size->setItemText(5, QCoreApplication::translate("MainWindow", "5", nullptr));
        cb_tile_size->setItemText(6, QCoreApplication::translate("MainWindow", "6", nullptr));
        cb_tile_size->setItemText(7, QCoreApplication::translate("MainWindow", "7", nullptr));
        cb_tile_size->setItemText(8, QCoreApplication::translate("MainWindow", "8", nullptr));
        cb_tile_size->setItemText(9, QCoreApplication::translate("MainWindow", "9", nullptr));
        cb_tile_size->setItemText(10, QCoreApplication::translate("MainWindow", "10", nullptr));
        cb_tile_size->setItemText(11, QCoreApplication::translate("MainWindow", "11", nullptr));
        cb_tile_size->setItemText(12, QCoreApplication::translate("MainWindow", "12", nullptr));
        cb_tile_size->setItemText(13, QCoreApplication::translate("MainWindow", "13", nullptr));
        cb_tile_size->setItemText(14, QCoreApplication::translate("MainWindow", "14", nullptr));
        cb_tile_size->setItemText(15, QCoreApplication::translate("MainWindow", "15", nullptr));
        cb_tile_size->setItemText(16, QCoreApplication::translate("MainWindow", "16", nullptr));
        cb_tile_size->setItemText(17, QCoreApplication::translate("MainWindow", "17", nullptr));
        cb_tile_size->setItemText(18, QCoreApplication::translate("MainWindow", "18", nullptr));
        cb_tile_size->setItemText(19, QCoreApplication::translate("MainWindow", "19", nullptr));
        cb_tile_size->setItemText(20, QCoreApplication::translate("MainWindow", "20", nullptr));
        cb_tile_size->setItemText(21, QCoreApplication::translate("MainWindow", "21", nullptr));
        cb_tile_size->setItemText(22, QCoreApplication::translate("MainWindow", "22", nullptr));
        cb_tile_size->setItemText(23, QCoreApplication::translate("MainWindow", "23", nullptr));
        cb_tile_size->setItemText(24, QCoreApplication::translate("MainWindow", "24", nullptr));
        cb_tile_size->setItemText(25, QCoreApplication::translate("MainWindow", "25", nullptr));
        cb_tile_size->setItemText(26, QCoreApplication::translate("MainWindow", "26", nullptr));
        cb_tile_size->setItemText(27, QCoreApplication::translate("MainWindow", "27", nullptr));
        cb_tile_size->setItemText(28, QCoreApplication::translate("MainWindow", "28", nullptr));
        cb_tile_size->setItemText(29, QCoreApplication::translate("MainWindow", "29", nullptr));
        cb_tile_size->setItemText(30, QCoreApplication::translate("MainWindow", "30", nullptr));
        cb_tile_size->setItemText(31, QCoreApplication::translate("MainWindow", "31", nullptr));
        cb_tile_size->setItemText(32, QCoreApplication::translate("MainWindow", "32", nullptr));

        label_5->setText(QCoreApplication::translate("MainWindow", "Model name", nullptr));
        cb_model_name->setItemText(0, QCoreApplication::translate("MainWindow", "realesr-animevideov3", nullptr));
        cb_model_name->setItemText(1, QCoreApplication::translate("MainWindow", "realesrgan-x4plus", nullptr));
        cb_model_name->setItemText(2, QCoreApplication::translate("MainWindow", "realesrgan-x4plus-anime", nullptr));

        label_3->setText(QCoreApplication::translate("MainWindow", "TTA Mode", nullptr));
        checkBox->setText(QCoreApplication::translate("MainWindow", "TTA mode", nullptr));
        label_6->setText(QCoreApplication::translate("MainWindow", "Jpg optimize", nullptr));
        cb_jpg_optimize->setItemText(0, QCoreApplication::translate("MainWindow", "100 (OFF)", nullptr));
        cb_jpg_optimize->setItemText(1, QCoreApplication::translate("MainWindow", "99", nullptr));
        cb_jpg_optimize->setItemText(2, QCoreApplication::translate("MainWindow", "98", nullptr));
        cb_jpg_optimize->setItemText(3, QCoreApplication::translate("MainWindow", "97", nullptr));
        cb_jpg_optimize->setItemText(4, QCoreApplication::translate("MainWindow", "96", nullptr));
        cb_jpg_optimize->setItemText(5, QCoreApplication::translate("MainWindow", "95", nullptr));
        cb_jpg_optimize->setItemText(6, QCoreApplication::translate("MainWindow", "94", nullptr));
        cb_jpg_optimize->setItemText(7, QCoreApplication::translate("MainWindow", "93", nullptr));
        cb_jpg_optimize->setItemText(8, QCoreApplication::translate("MainWindow", "92", nullptr));
        cb_jpg_optimize->setItemText(9, QCoreApplication::translate("MainWindow", "91", nullptr));
        cb_jpg_optimize->setItemText(10, QCoreApplication::translate("MainWindow", "90", nullptr));
        cb_jpg_optimize->setItemText(11, QCoreApplication::translate("MainWindow", "89", nullptr));
        cb_jpg_optimize->setItemText(12, QCoreApplication::translate("MainWindow", "88", nullptr));
        cb_jpg_optimize->setItemText(13, QCoreApplication::translate("MainWindow", "87", nullptr));
        cb_jpg_optimize->setItemText(14, QCoreApplication::translate("MainWindow", "86", nullptr));
        cb_jpg_optimize->setItemText(15, QCoreApplication::translate("MainWindow", "85", nullptr));
        cb_jpg_optimize->setItemText(16, QCoreApplication::translate("MainWindow", "84", nullptr));
        cb_jpg_optimize->setItemText(17, QCoreApplication::translate("MainWindow", "83", nullptr));
        cb_jpg_optimize->setItemText(18, QCoreApplication::translate("MainWindow", "82", nullptr));
        cb_jpg_optimize->setItemText(19, QCoreApplication::translate("MainWindow", "81", nullptr));
        cb_jpg_optimize->setItemText(20, QCoreApplication::translate("MainWindow", "80", nullptr));
        cb_jpg_optimize->setItemText(21, QCoreApplication::translate("MainWindow", "79", nullptr));
        cb_jpg_optimize->setItemText(22, QCoreApplication::translate("MainWindow", "78", nullptr));
        cb_jpg_optimize->setItemText(23, QCoreApplication::translate("MainWindow", "77", nullptr));
        cb_jpg_optimize->setItemText(24, QCoreApplication::translate("MainWindow", "76", nullptr));
        cb_jpg_optimize->setItemText(25, QCoreApplication::translate("MainWindow", "75", nullptr));

        pushButton_2->setText(QCoreApplication::translate("MainWindow", "Add folder", nullptr));
        pushButton_3->setText(QCoreApplication::translate("MainWindow", "Add file", nullptr));
        btn_start->setText(QCoreApplication::translate("MainWindow", "Start", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
