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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 598)
        MainWindow.setStyleSheet(u"#centralwidget{\n"
"background-color: white;\n"
"}")
        self.actionEnglish = QAction(MainWindow)
        self.actionEnglish.setObjectName(u"actionEnglish")
        self.actionFrench = QAction(MainWindow)
        self.actionFrench.setObjectName(u"actionFrench")
        self.actionArabic = QAction(MainWindow)
        self.actionArabic.setObjectName(u"actionArabic")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QLineEdit {\n"
"color: red;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftMenuBar = QWidget(self.centralwidget)
        self.leftMenuBar.setObjectName(u"leftMenuBar")
        self.leftMenuBar.setStyleSheet(u"#leftMenuBar {\n"
"background-color: #101010;\n"
"}\n"
"\n"
"QLabel {\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: #101010;\n"
"color: white;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #304030;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"background-color: #303030;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.leftMenuBar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.menuTitle = QFrame(self.leftMenuBar)
        self.menuTitle.setObjectName(u"menuTitle")
        self.menuTitle.setFrameShape(QFrame.StyledPanel)
        self.menuTitle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.menuTitle)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.titleLabel = QLabel(self.menuTitle)
        self.titleLabel.setObjectName(u"titleLabel")
        font = QFont()
        font.setFamilies([u"Yu Gothic UI Semibold"])
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        self.titleLabel.setFont(font)

        self.horizontalLayout_2.addWidget(self.titleLabel, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.menuTitle, 0, Qt.AlignTop)

        self.menu = QFrame(self.leftMenuBar)
        self.menu.setObjectName(u"menu")
        self.menu.setFrameShape(QFrame.StyledPanel)
        self.menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.searchMenuButton = QPushButton(self.menu)
        self.searchMenuButton.setObjectName(u"searchMenuButton")
        self.searchMenuButton.setMinimumSize(QSize(0, 35))
        font1 = QFont()
        font1.setFamilies([u"Yu Gothic UI Semibold"])
        font1.setPointSize(12)
        self.searchMenuButton.setFont(font1)
        self.searchMenuButton.setCheckable(True)
        self.searchMenuButton.setChecked(True)
        self.searchMenuButton.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.searchMenuButton)

        self.readButton = QPushButton(self.menu)
        self.readButton.setObjectName(u"readButton")
        self.readButton.setMinimumSize(QSize(0, 35))
        self.readButton.setFont(font1)
        self.readButton.setCheckable(True)
        self.readButton.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.readButton)

        self.settingsButton = QPushButton(self.menu)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setMinimumSize(QSize(0, 35))
        self.settingsButton.setFont(font1)
        self.settingsButton.setCheckable(True)
        self.settingsButton.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.settingsButton)


        self.verticalLayout.addWidget(self.menu, 0, Qt.AlignVCenter)


        self.horizontalLayout.addWidget(self.leftMenuBar)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"\n"
"	background-color: white;")
        self.searchPage = QWidget()
        self.searchPage.setObjectName(u"searchPage")
        self.gridLayout = QGridLayout(self.searchPage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.mainContent = QWidget(self.searchPage)
        self.mainContent.setObjectName(u"mainContent")
        self.mainContent.setStyleSheet(u"QPushButton {\n"
"border: none;\n"
"background-color: #E66189;\n"
"}\n"
"\n"
"QPushButton: hover {\n"
"background-color: #EE96B0;\n"
"}")
        self.tableWidget = QTableWidget(self.mainContent)
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
        self.tableWidget.setGeometry(QRect(1, 250, 621, 271))
        self.listLabel = QLabel(self.mainContent)
        self.listLabel.setObjectName(u"listLabel")
        self.listLabel.setGeometry(QRect(3, 225, 140, 21))
        font2 = QFont()
        font2.setFamilies([u"Yu Gothic UI Semibold"])
        font2.setPointSize(10)
        self.listLabel.setFont(font2)
        self.messagesLabel = QLabel(self.mainContent)
        self.messagesLabel.setObjectName(u"messagesLabel")
        self.messagesLabel.setGeometry(QRect(520, 30, 271, 171))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.messagesLabel.sizePolicy().hasHeightForWidth())
        self.messagesLabel.setSizePolicy(sizePolicy)
        self.messagesLabel.setMinimumSize(QSize(0, 0))
        self.messagesLabel.setStyleSheet(u"background-color: White")
        self.messagesLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.layoutWidget = QWidget(self.mainContent)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 51, 483, 135))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.listNameLabel = QLabel(self.layoutWidget)
        self.listNameLabel.setObjectName(u"listNameLabel")
        self.listNameLabel.setFont(font2)

        self.horizontalLayout_3.addWidget(self.listNameLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.listNameEdit = QLineEdit(self.layoutWidget)
        self.listNameEdit.setObjectName(u"listNameEdit")
        self.listNameEdit.setMinimumSize(QSize(300, 40))
        self.listNameEdit.setMaximumSize(QSize(16777215, 16777215))
        self.listNameEdit.setSizeIncrement(QSize(0, 34))
        font3 = QFont()
        font3.setPointSize(9)
        self.listNameEdit.setFont(font3)

        self.horizontalLayout_3.addWidget(self.listNameEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)

        self.horizontalLayout_4.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.searchEdit = QLineEdit(self.layoutWidget)
        self.searchEdit.setObjectName(u"searchEdit")
        self.searchEdit.setMinimumSize(QSize(300, 40))
        self.searchEdit.setMaximumSize(QSize(16777215, 16777215))
        self.searchEdit.setSizeIncrement(QSize(0, 34))

        self.horizontalLayout_4.addWidget(self.searchEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.buttonsContainer = QHBoxLayout()
        self.buttonsContainer.setObjectName(u"buttonsContainer")
        self.searchButton = QPushButton(self.layoutWidget)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setMinimumSize(QSize(0, 35))
        self.searchButton.setMaximumSize(QSize(16777215, 45))
        font4 = QFont()
        font4.setPointSize(12)
        self.searchButton.setFont(font4)

        self.buttonsContainer.addWidget(self.searchButton)

        self.stopScrapingButton = QPushButton(self.layoutWidget)
        self.stopScrapingButton.setObjectName(u"stopScrapingButton")
        self.stopScrapingButton.setMinimumSize(QSize(0, 34))
        self.stopScrapingButton.setMaximumSize(QSize(16777215, 45))
        self.stopScrapingButton.setFont(font4)

        self.buttonsContainer.addWidget(self.stopScrapingButton)


        self.verticalLayout_3.addLayout(self.buttonsContainer)

        self.saveListButton = QPushButton(self.mainContent)
        self.saveListButton.setObjectName(u"saveListButton")
        self.saveListButton.setGeometry(QRect(630, 479, 40, 40))
        icon = QIcon()
        icon.addFile(u":/icons/C:/Users/ahmed/Downloads/feather icons/save.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.saveListButton.setIcon(icon)
        self.saveListButton.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.mainContent, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.searchPage)
        self.readPage = QWidget()
        self.readPage.setObjectName(u"readPage")
        self.gridLayout_2 = QGridLayout(self.readPage)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(self.readPage)
        self.label_3.setObjectName(u"label_3")
        font5 = QFont()
        font5.setPointSize(40)
        self.label_3.setFont(font5)

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.readPage)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.label_4 = QLabel(self.settingsPage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(180, 220, 341, 71))
        self.label_4.setFont(font5)
        self.stackedWidget.addWidget(self.settingsPage)

        self.horizontalLayout.addWidget(self.stackedWidget)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1024, 22))
        self.menuLanguages = QMenu(self.menubar)
        self.menuLanguages.setObjectName(u"menuLanguages")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuLanguages.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuLanguages.addAction(self.actionEnglish)
        self.menuLanguages.addAction(self.actionFrench)
        self.menuLanguages.addAction(self.actionArabic)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Place finder", None))
        self.actionEnglish.setText(QCoreApplication.translate("MainWindow", u"English", None))
        self.actionFrench.setText(QCoreApplication.translate("MainWindow", u"Fran\u00e7ais", None))
        self.actionArabic.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0639\u0631\u0628\u064a\u0629", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"Places Finder", None))
        self.searchMenuButton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.readButton.setText(QCoreApplication.translate("MainWindow", u"Read", None))
        self.settingsButton.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Telephone", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Maps", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Website", None));
        self.listLabel.setText(QCoreApplication.translate("MainWindow", u"Search list", None))
        self.messagesLabel.setText("")
        self.listNameLabel.setText(QCoreApplication.translate("MainWindow", u"List name", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Enter a query here", None))
        self.searchButton.setText(QCoreApplication.translate("MainWindow", u"Start searching", None))
        self.stopScrapingButton.setText(QCoreApplication.translate("MainWindow", u"Stop searching", None))
        self.saveListButton.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Read Page", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Settings Page", None))
        self.menuLanguages.setTitle(QCoreApplication.translate("MainWindow", u"Languages", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

