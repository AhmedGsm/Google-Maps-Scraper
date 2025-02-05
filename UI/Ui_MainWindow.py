# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'goomaps.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(572, 310)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 41, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalSpacer_3 = QSpacerItem(20, 42, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(11)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.searchEdit = QLineEdit(self.centralwidget)
        self.searchEdit.setObjectName(u"searchEdit")
        self.searchEdit.setMinimumSize(QSize(0, 40))
        self.searchEdit.setMaximumSize(QSize(16777215, 16777215))
        self.searchEdit.setSizeIncrement(QSize(0, 40))

        self.verticalLayout.addWidget(self.searchEdit)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.searchButton = QPushButton(self.centralwidget)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setMinimumSize(QSize(0, 45))
        self.searchButton.setMaximumSize(QSize(16777215, 45))
        font1 = QFont()
        font1.setPointSize(12)
        self.searchButton.setFont(font1)

        self.horizontalLayout_3.addWidget(self.searchButton)

        self.searchButton_2 = QPushButton(self.centralwidget)
        self.searchButton_2.setObjectName(u"searchButton_2")
        self.searchButton_2.setMinimumSize(QSize(0, 45))
        self.searchButton_2.setMaximumSize(QSize(16777215, 45))
        self.searchButton_2.setFont(font1)

        self.horizontalLayout_3.addWidget(self.searchButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 41, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 572, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Enter a query here", None))
        self.searchButton.setText(QCoreApplication.translate("MainWindow", u"Start scraping!", None))
        self.searchButton_2.setText(QCoreApplication.translate("MainWindow", u"Stop scraping", None))
    # retranslateUi

