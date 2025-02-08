import sys
import threading
import time

from Ui_MainWindow import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow

from constants import *
from drivermanipulator import DriverManipulator
from wsite import Site

class WindowApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.driver_manipulator = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.searchButton.clicked.connect(self.on_searchButton_clicked)
        self.ui.stopScrapingButton.clicked.connect(self.on_stopScrapingButton_clicked)
        self.ui.searchEdit.textChanged.connect(self.on_searchEdit_changed)
        self.ui.searchEdit.returnPressed.connect(self.on_searchEdit_returnPressed)
        # Disable Stop scraping button
        self.ui.searchButton.setEnabled(False)
        self.ui.stopScrapingButton.setEnabled(False)
        # Insert a text inside a edit search
        #self.ui.searchEdit.setText("Plomberie à Reghaia")
        self.stopButtonText = self.ui.stopScrapingButton.text()
        self.startButtonText = self.ui.searchButton.text()

    def on_searchButton_clicked(self):
        self.startScrapingThread = threading.Thread(target=self.startScraping)
        self.startScrapingThread.start()
        # Disable search button
        ui_text = "Start scraping..."
        self.ui.searchButton.setText(ui_text)
        self.append_label_inline_text(self.ui.messagesLabel, ui_text)
        self.ui.searchButton.setEnabled(False)
        self.ui.stopScrapingButton.setEnabled(True)

    def on_stopScrapingButton_clicked(self):
        stopScrapingThread = threading.Thread(target=self.stopScraping)
        stopScrapingThread.start()
        ui_text = "Stopping scraping..."
        self.ui.stopScrapingButton.setText(ui_text)
        self.append_label_inline_text(self.ui.messagesLabel, ui_text)
        self.ui.stopScrapingButton.setEnabled(False)
        self.ui.searchButton.setText(self.startButtonText)

    def startScraping(self):
        self.driver_manipulator = DriverManipulator()
        self.googlemapssite = Site(self.driver_manipulator)
        self.googlemapssite.scrape_site(self.ui.searchEdit.text())
        self.driver_manipulator.quit_driver()
        # Quit the second driver(edge)
        self.googlemapssite.manipulator.quit_driver()
        # Change buttons states and textes
        self.ui.stopScrapingButton.setEnabled(False)
        self.ui.searchButton.setEnabled(True)
        self.append_label_inline_text(self.ui.messagesLabel, "Scraping is stopped")
        self.ui.searchButton.setText(self.startButtonText)
        self.ui.stopScrapingButton.setText(self.stopButtonText)

    def stopScraping(self):
        self.googlemapssite.stop_scraping()
        # Quit first and second drivers
        time.sleep(2)

    def on_searchEdit_changed(self, newText):
        self.ui.searchButton.setEnabled(False)
        if newText:
            self.ui.searchButton.setEnabled(True)


    def on_searchEdit_returnPressed(self):
        text = self.ui.searchEdit.text()
        if self.ui.searchEdit.text():
            self.on_searchButton_clicked()

    def append_label_inline_text(self, qLabel, text):
        # If the label is already have a text
        # then append the text to the next line!
        if qLabel.text():
            qLabel.setText(f"{qLabel.text()}\n{text}")
        else:
            qLabel.setText(text)




myApp = QApplication(sys.argv)
window = WindowApp()
window.show()
myApp.exit(myApp.exec())