# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_about.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(559, 403)
        Dialog.setStyleSheet(u"\n"
"    QLabel {\n"
"        font-size: 14px;\n"
"    }\n"
"    QPushButton {\n"
"        background-color: #4CAF50;\n"
"        color: white;\n"
"        padding: 8px;\n"
"        border-radius: 5px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: #45a049;\n"
"    }\n"
"\n"
"")
        self.buttonOk = QPushButton(Dialog)
        self.buttonOk.setObjectName(u"buttonOk")
        self.buttonOk.setGeometry(QRect(240, 350, 75, 31))
        self.logoLabel = QLabel(Dialog)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setGeometry(QRect(40, 40, 101, 101))
        self.logoLabel.setStyleSheet(u"background-color: White")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(230, 40, 248, 171))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.appName = QLabel(self.widget)
        self.appName.setObjectName(u"appName")
        font = QFont()
        font.setFamilies([u"Century Gothic"])
        font.setBold(False)
        self.appName.setFont(font)

        self.verticalLayout.addWidget(self.appName)

        self.appName_2 = QLabel(self.widget)
        self.appName_2.setObjectName(u"appName_2")
        self.appName_2.setFont(font)

        self.verticalLayout.addWidget(self.appName_2)

        self.appName_3 = QLabel(self.widget)
        self.appName_3.setObjectName(u"appName_3")
        self.appName_3.setFont(font)

        self.verticalLayout.addWidget(self.appName_3)

        self.appName_4 = QLabel(self.widget)
        self.appName_4.setObjectName(u"appName_4")
        self.appName_4.setFont(font)
        self.appName_4.setOpenExternalLinks(True)

        self.verticalLayout.addWidget(self.appName_4)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.buttonOk.setText(QCoreApplication.translate("Dialog", u"Ok", None))
        self.logoLabel.setText("")
        self.appName.setText(QCoreApplication.translate("Dialog", u"Places Finder version 1.0", None))
        self.appName_2.setText(QCoreApplication.translate("Dialog", u"Developed by Ahmed KHABER", None))
        self.appName_3.setText(QCoreApplication.translate("Dialog", u"\u00a9 2025 Ibtikar. All Rights Reserved.", None))
        self.appName_4.setText(QCoreApplication.translate("Dialog", u"<a href=\"www.Ibtikar.com\">Visit Website</a>", None))
    # retranslateUi

