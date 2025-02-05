import sys
import threading

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

    def on_searchButton_clicked(self):
        print("on_searchButton_clicked clicked")
        startScrapingThread = threading.Thread(target=self.startScraping)
        startScrapingThread.start()
        #startScrapingThread.join()

    def on_stopScrapingButton_clicked(self):
        print("on_stopScrapingButton_clicked clicked")
        stopScrapingThread = threading.Thread(target=self.stopScraping)
        stopScrapingThread.start()
        stopScrapingThread.join()


    def startScraping(self):
        self.driver_manipulator = DriverManipulator()
        self.googlemapssite = Site(self.driver_manipulator)
        self.googlemapssite.scrape_site(self.ui.searchEdit.text())
        self.driver_manipulator.driver.quit()
        # Quit the second driver(edge)
        self.googlemapssite.manipulator.quit()

    def stopScraping(self):
        self.googlemapssite.stop_scraping()
        # Quit the second driver(edge)
        self.googlemapssite.manipulator.quit()
        self.driver_manipulator.driver.quit()



myApp = QApplication(sys.argv)
window = WindowApp()
window.show()
myApp.exit(myApp.exec())