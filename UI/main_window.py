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
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.searchButton.clicked.connect(self.on_searchButton_clicked)

    def on_searchButton_clicked(self):
        print("on_searchButton_clicked clicked")
        startScrapingThread = threading.Thread(target=self.startScraping)
        startScrapingThread.start()
        #startScrapingThread.join()

    def startScraping(self):
        driver_manipulator = DriverManipulator()
        googlemapssite = Site(driver_manipulator)
        googlemapssite.scrape_site(self.ui.searchEdit.text())
        input("Enter any key to exit!")
        driver_manipulator.driver.quit()



myApp = QApplication(sys.argv)
window = WindowApp()
window.show()
myApp.exit(myApp.exec())