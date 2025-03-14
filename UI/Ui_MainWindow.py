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
        MainWindow.resize(1103, 670)
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
"}\n"
"\n"
"#registerMessageLabel {\n"
"	color: #32BA12;\n"
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

        self.registerMenuButton = QPushButton(self.menu)
        self.registerMenuButton.setObjectName(u"registerMenuButton")
        self.registerMenuButton.setMinimumSize(QSize(0, 35))
        self.registerMenuButton.setFont(font1)
        self.registerMenuButton.setCheckable(True)
        self.registerMenuButton.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.registerMenuButton)

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
"QWidget {\n"
"	background-color: white;\n"
"}\n"
"\n"
"QPushButton {\n"
"border: none;\n"
"background-color: #E66189;\n"
"}\n"
"\n"
"QPushButton: hover {\n"
"background-color: #EE96B0;\n"
"}")
        self.searchPage = QWidget()
        self.searchPage.setObjectName(u"searchPage")
        self.searchPage.setEnabled(False)
        self.gridLayout = QGridLayout(self.searchPage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.mainContent = QWidget(self.searchPage)
        self.mainContent.setObjectName(u"mainContent")
        self.mainContent.setStyleSheet(u"#userInfosFrame, #messagesLabel {\n"
"	border: 1px solid #CACACA;\n"
"\n"
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
        self.tableWidget.setGeometry(QRect(1, 286, 531, 271))
        self.listLabel = QLabel(self.mainContent)
        self.listLabel.setObjectName(u"listLabel")
        self.listLabel.setGeometry(QRect(3, 261, 140, 21))
        font2 = QFont()
        font2.setFamilies([u"Yu Gothic UI Semibold"])
        font2.setPointSize(10)
        self.listLabel.setFont(font2)
        self.messagesLabel = QLabel(self.mainContent)
        self.messagesLabel.setObjectName(u"messagesLabel")
        self.messagesLabel.setGeometry(QRect(550, 286, 221, 241))
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
        self.layoutWidget.setGeometry(QRect(0, 51, 483, 161))
        self.searchFormLayout = QVBoxLayout(self.layoutWidget)
        self.searchFormLayout.setObjectName(u"searchFormLayout")
        self.searchFormLayout.setContentsMargins(0, 0, 0, 0)
        self.topHorizontalLayout = QHBoxLayout()
        self.topHorizontalLayout.setObjectName(u"topHorizontalLayout")
        self.listNameLabel = QLabel(self.layoutWidget)
        self.listNameLabel.setObjectName(u"listNameLabel")
        self.listNameLabel.setFont(font2)

        self.topHorizontalLayout.addWidget(self.listNameLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.topHorizontalLayout.addItem(self.horizontalSpacer)

        self.listNameEdit = QLineEdit(self.layoutWidget)
        self.listNameEdit.setObjectName(u"listNameEdit")
        self.listNameEdit.setEnabled(False)
        self.listNameEdit.setMinimumSize(QSize(300, 40))
        self.listNameEdit.setMaximumSize(QSize(16777215, 16777215))
        self.listNameEdit.setSizeIncrement(QSize(0, 34))
        font3 = QFont()
        font3.setPointSize(9)
        self.listNameEdit.setFont(font3)

        self.topHorizontalLayout.addWidget(self.listNameEdit)


        self.searchFormLayout.addLayout(self.topHorizontalLayout)

        self.bottomHorizontalLayout = QHBoxLayout()
        self.bottomHorizontalLayout.setObjectName(u"bottomHorizontalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)

        self.bottomHorizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.bottomHorizontalLayout.addItem(self.horizontalSpacer_2)

        self.searchEdit = QLineEdit(self.layoutWidget)
        self.searchEdit.setObjectName(u"searchEdit")
        self.searchEdit.setMinimumSize(QSize(300, 40))
        self.searchEdit.setMaximumSize(QSize(16777215, 16777215))
        self.searchEdit.setSizeIncrement(QSize(0, 34))

        self.bottomHorizontalLayout.addWidget(self.searchEdit)


        self.searchFormLayout.addLayout(self.bottomHorizontalLayout)

        self.buttonsContainer = QHBoxLayout()
        self.buttonsContainer.setObjectName(u"buttonsContainer")
        self.buttonsContainer.setContentsMargins(-1, -1, -1, 0)
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


        self.searchFormLayout.addLayout(self.buttonsContainer)

        self.saveListButton = QPushButton(self.mainContent)
        self.saveListButton.setObjectName(u"saveListButton")
        self.saveListButton.setEnabled(False)
        self.saveListButton.setGeometry(QRect(0, 566, 40, 40))
        icon = QIcon()
        icon.addFile(u":/icons/C:/Users/ahmed/Downloads/feather icons/save.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.saveListButton.setIcon(icon)
        self.saveListButton.setIconSize(QSize(32, 32))
        self.userInfosFrame = QFrame(self.mainContent)
        self.userInfosFrame.setObjectName(u"userInfosFrame")
        self.userInfosFrame.setGeometry(QRect(500, 50, 281, 161))
        self.userInfosFrame.setStyleSheet(u"")
        self.userInfosFrame.setFrameShape(QFrame.StyledPanel)
        self.userInfosFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.userInfosFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.userInfosLayout = QHBoxLayout()
        self.userInfosLayout.setObjectName(u"userInfosLayout")
        self.labelsVLayout = QVBoxLayout()
        self.labelsVLayout.setObjectName(u"labelsVLayout")
        self.nameLabel = QLabel(self.userInfosFrame)
        self.nameLabel.setObjectName(u"nameLabel")
        font5 = QFont()
        font5.setPointSize(9)
        font5.setBold(True)
        self.nameLabel.setFont(font5)

        self.labelsVLayout.addWidget(self.nameLabel)

        self.nameLabel_2 = QLabel(self.userInfosFrame)
        self.nameLabel_2.setObjectName(u"nameLabel_2")
        self.nameLabel_2.setFont(font5)

        self.labelsVLayout.addWidget(self.nameLabel_2)

        self.creditsLabel = QLabel(self.userInfosFrame)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setFont(font5)

        self.labelsVLayout.addWidget(self.creditsLabel)

        self.licenseLabel = QLabel(self.userInfosFrame)
        self.licenseLabel.setObjectName(u"licenseLabel")
        self.licenseLabel.setFont(font5)

        self.labelsVLayout.addWidget(self.licenseLabel)

        self.dueLabel = QLabel(self.userInfosFrame)
        self.dueLabel.setObjectName(u"dueLabel")
        self.dueLabel.setFont(font5)

        self.labelsVLayout.addWidget(self.dueLabel)


        self.userInfosLayout.addLayout(self.labelsVLayout)

        self.userInfosVLayout = QVBoxLayout()
        self.userInfosVLayout.setObjectName(u"userInfosVLayout")
        self.nameValue = QLabel(self.userInfosFrame)
        self.nameValue.setObjectName(u"nameValue")

        self.userInfosVLayout.addWidget(self.nameValue)

        self.emailValue = QLabel(self.userInfosFrame)
        self.emailValue.setObjectName(u"emailValue")

        self.userInfosVLayout.addWidget(self.emailValue)

        self.creditsValue = QLabel(self.userInfosFrame)
        self.creditsValue.setObjectName(u"creditsValue")

        self.userInfosVLayout.addWidget(self.creditsValue)

        self.licenseValue = QLabel(self.userInfosFrame)
        self.licenseValue.setObjectName(u"licenseValue")

        self.userInfosVLayout.addWidget(self.licenseValue)

        self.dueValue = QLabel(self.userInfosFrame)
        self.dueValue.setObjectName(u"dueValue")

        self.userInfosVLayout.addWidget(self.dueValue)


        self.userInfosLayout.addLayout(self.userInfosVLayout)

        self.userInfosLayout.setStretch(0, 1)
        self.userInfosLayout.setStretch(1, 3)

        self.gridLayout_2.addLayout(self.userInfosLayout, 0, 0, 1, 1)

        self.licenseStatusLabel = QLabel(self.mainContent)
        self.licenseStatusLabel.setObjectName(u"licenseStatusLabel")
        self.licenseStatusLabel.setGeometry(QRect(3, 225, 771, 18))
        font6 = QFont()
        font6.setPointSize(11)
        font6.setBold(True)
        self.licenseStatusLabel.setFont(font6)
        self.licenseStatusLabel.setStyleSheet(u"color: #1AF3BA")

        self.gridLayout.addWidget(self.mainContent, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.searchPage)
        self.registerPage = QWidget()
        self.registerPage.setObjectName(u"registerPage")
        self.registerHeaderLabel = QLabel(self.registerPage)
        self.registerHeaderLabel.setObjectName(u"registerHeaderLabel")
        self.registerHeaderLabel.setGeometry(QRect(270, 90, 158, 36))
        font7 = QFont()
        font7.setPointSize(20)
        self.registerHeaderLabel.setFont(font7)
        self.layoutWidget_2 = QWidget(self.registerPage)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(141, 181, 411, 42))
        self.inputContainer = QHBoxLayout(self.layoutWidget_2)
        self.inputContainer.setObjectName(u"inputContainer")
        self.inputContainer.setContentsMargins(0, 0, 0, 0)
        self.listNameLabel_2 = QLabel(self.layoutWidget_2)
        self.listNameLabel_2.setObjectName(u"listNameLabel_2")
        self.listNameLabel_2.setFont(font2)

        self.inputContainer.addWidget(self.listNameLabel_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.inputContainer.addItem(self.horizontalSpacer_3)

        self.nameEdit = QLineEdit(self.layoutWidget_2)
        self.nameEdit.setObjectName(u"nameEdit")
        self.nameEdit.setMinimumSize(QSize(300, 40))
        self.nameEdit.setMaximumSize(QSize(16777215, 16777215))
        self.nameEdit.setSizeIncrement(QSize(0, 34))
        self.nameEdit.setFont(font3)

        self.inputContainer.addWidget(self.nameEdit)

        self.layoutWidget_3 = QWidget(self.registerPage)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(140, 260, 412, 42))
        self.inputContainer_2 = QHBoxLayout(self.layoutWidget_3)
        self.inputContainer_2.setObjectName(u"inputContainer_2")
        self.inputContainer_2.setContentsMargins(0, 0, 0, 0)
        self.listNameLabel_3 = QLabel(self.layoutWidget_3)
        self.listNameLabel_3.setObjectName(u"listNameLabel_3")
        self.listNameLabel_3.setFont(font2)

        self.inputContainer_2.addWidget(self.listNameLabel_3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.inputContainer_2.addItem(self.horizontalSpacer_4)

        self.emailEdit = QLineEdit(self.layoutWidget_3)
        self.emailEdit.setObjectName(u"emailEdit")
        self.emailEdit.setMinimumSize(QSize(300, 40))
        self.emailEdit.setMaximumSize(QSize(16777215, 16777215))
        self.emailEdit.setSizeIncrement(QSize(0, 34))
        self.emailEdit.setFont(font3)

        self.inputContainer_2.addWidget(self.emailEdit)

        self.layoutWidget_4 = QWidget(self.registerPage)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(140, 342, 412, 42))
        self.inputContainer_3 = QHBoxLayout(self.layoutWidget_4)
        self.inputContainer_3.setObjectName(u"inputContainer_3")
        self.inputContainer_3.setContentsMargins(0, 0, 0, 0)
        self.listNameLabel_4 = QLabel(self.layoutWidget_4)
        self.listNameLabel_4.setObjectName(u"listNameLabel_4")
        self.listNameLabel_4.setFont(font2)

        self.inputContainer_3.addWidget(self.listNameLabel_4)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.inputContainer_3.addItem(self.horizontalSpacer_5)

        self.phoneEdit = QLineEdit(self.layoutWidget_4)
        self.phoneEdit.setObjectName(u"phoneEdit")
        self.phoneEdit.setMinimumSize(QSize(300, 40))
        self.phoneEdit.setMaximumSize(QSize(16777215, 16777215))
        self.phoneEdit.setSizeIncrement(QSize(0, 34))
        self.phoneEdit.setFont(font3)

        self.inputContainer_3.addWidget(self.phoneEdit)

        self.registerButton = QPushButton(self.registerPage)
        self.registerButton.setObjectName(u"registerButton")
        self.registerButton.setEnabled(False)
        self.registerButton.setGeometry(QRect(140, 420, 411, 45))
        self.registerButton.setMinimumSize(QSize(0, 35))
        self.registerButton.setMaximumSize(QSize(16777215, 45))
        self.registerButton.setFont(font4)
        self.nameMessageLabel = QLabel(self.registerPage)
        self.nameMessageLabel.setObjectName(u"nameMessageLabel")
        self.nameMessageLabel.setGeometry(QRect(250, 226, 431, 16))
        self.emailMessageLabel = QLabel(self.registerPage)
        self.emailMessageLabel.setObjectName(u"emailMessageLabel")
        self.emailMessageLabel.setGeometry(QRect(252, 307, 421, 16))
        self.phoneMessageLabel = QLabel(self.registerPage)
        self.phoneMessageLabel.setObjectName(u"phoneMessageLabel")
        self.phoneMessageLabel.setGeometry(QRect(252, 387, 391, 16))
        self.registerMessageLabel = QLabel(self.registerPage)
        self.registerMessageLabel.setObjectName(u"registerMessageLabel")
        self.registerMessageLabel.setGeometry(QRect(140, 480, 411, 51))
        font8 = QFont()
        font8.setPointSize(11)
        self.registerMessageLabel.setFont(font8)
        self.registerMessageLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.stackedWidget.addWidget(self.registerPage)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.label_4 = QLabel(self.settingsPage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(180, 220, 341, 71))
        font9 = QFont()
        font9.setPointSize(40)
        self.label_4.setFont(font9)
        self.stackedWidget.addWidget(self.settingsPage)

        self.horizontalLayout.addWidget(self.stackedWidget)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1103, 22))
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
        self.registerMenuButton.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.settingsButton.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
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
        self.listLabel.setText(QCoreApplication.translate("MainWindow", u"Search list", None))
        self.messagesLabel.setText("")
        self.listNameLabel.setText(QCoreApplication.translate("MainWindow", u"List name", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Enter a query here", None))
        self.searchButton.setText(QCoreApplication.translate("MainWindow", u"Start searching", None))
        self.stopScrapingButton.setText(QCoreApplication.translate("MainWindow", u"Stop searching", None))
        self.saveListButton.setText("")
        self.nameLabel.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.nameLabel_2.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"Credits", None))
        self.licenseLabel.setText(QCoreApplication.translate("MainWindow", u"License", None))
        self.dueLabel.setText(QCoreApplication.translate("MainWindow", u"License Due", None))
        self.nameValue.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.emailValue.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.creditsValue.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.licenseValue.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.dueValue.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.licenseStatusLabel.setText(QCoreApplication.translate("MainWindow", u"Go to Register page to register", None))
        self.registerHeaderLabel.setText(QCoreApplication.translate("MainWindow", u"Register Now", None))
        self.listNameLabel_2.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.listNameLabel_3.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.listNameLabel_4.setText(QCoreApplication.translate("MainWindow", u"Phone", None))
        self.registerButton.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.nameMessageLabel.setText(QCoreApplication.translate("MainWindow", u"This field is required", None))
        self.emailMessageLabel.setText(QCoreApplication.translate("MainWindow", u"This field is required", None))
        self.phoneMessageLabel.setText(QCoreApplication.translate("MainWindow", u"This field is required", None))
        self.registerMessageLabel.setText(QCoreApplication.translate("MainWindow", u"Fill all above fields then click register button", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Settings Page", None))
        self.menuLanguages.setTitle(QCoreApplication.translate("MainWindow", u"Languages", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

