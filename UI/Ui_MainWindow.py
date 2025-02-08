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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(572, 559)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 80, 120, 20))
        font = QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.searchEdit = QLineEdit(self.centralwidget)
        self.searchEdit.setObjectName(u"searchEdit")
        self.searchEdit.setGeometry(QRect(9, 107, 291, 41))
        self.searchEdit.setMinimumSize(QSize(0, 40))
        self.searchEdit.setMaximumSize(QSize(16777215, 16777215))
        self.searchEdit.setSizeIncrement(QSize(0, 40))
        self.messagesLabel = QLabel(self.centralwidget)
        self.messagesLabel.setObjectName(u"messagesLabel")
        self.messagesLabel.setGeometry(QRect(330, 20, 221, 171))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.messagesLabel.sizePolicy().hasHeightForWidth())
        self.messagesLabel.setSizePolicy(sizePolicy)
        self.messagesLabel.setMinimumSize(QSize(0, 0))
        self.messagesLabel.setStyleSheet(u"background-color: White")
        self.messagesLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 250, 531, 271))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 230, 120, 20))
        self.label_2.setFont(font)
        self.searchButton = QPushButton(self.centralwidget)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setGeometry(QRect(10, 160, 131, 35))
        self.searchButton.setMinimumSize(QSize(0, 35))
        self.searchButton.setMaximumSize(QSize(16777215, 45))
        font1 = QFont()
        font1.setPointSize(12)
        self.searchButton.setFont(font1)
        self.stopScrapingButton = QPushButton(self.centralwidget)
        self.stopScrapingButton.setObjectName(u"stopScrapingButton")
        self.stopScrapingButton.setGeometry(QRect(158, 160, 141, 34))
        self.stopScrapingButton.setMinimumSize(QSize(0, 34))
        self.stopScrapingButton.setMaximumSize(QSize(16777215, 45))
        self.stopScrapingButton.setFont(font1)
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
        self.messagesLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Telephone", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Website", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Maps", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Enter a query here", None))
        self.searchButton.setText(QCoreApplication.translate("MainWindow", u"Start scraping!", None))
        self.stopScrapingButton.setText(QCoreApplication.translate("MainWindow", u"Stop scraping", None))
    # retranslateUi

