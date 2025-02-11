import sys
import threading
import time

from UI.dialog_about import dialog_about
from Ui_MainWindow import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import QTranslator, QLocale, QCoreApplication
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
        # Menu Actions
        self.translator = QTranslator()

        # Connect menu actions to functions
        self.ui.actionEnglish.triggered.connect(lambda: self.change_language("en"))
        self.ui.actionFrench.triggered.connect(lambda: self.change_language("fr"))
        self.ui.actionArabic.triggered.connect(lambda: self.change_language("ar"))        # Disable Stop scraping button
        self.ui.actionAbout.triggered.connect(lambda: self.display_help_dialog())
        self.ui.searchButton.setEnabled(False)
        self.ui.stopScrapingButton.setEnabled(False)
        # Insert a text inside a edit search
        #self.ui.searchEdit.setText("Plomberie à Reghaia")
        self.stopButtonText = self.ui.stopScrapingButton.text()
        self.startButtonText = self.ui.searchButton.text()

        self.translate_UI()

    def translate_UI(self):
        # Load translation
        #self.translator = QTranslator()
        #if self.translator.load("translation/translations_ar.qm"):  # Load the translation file
        #    app.installTranslator(self.translator)
        # Apply translations
        self.ui.retranslateUi(self)

    def on_searchButton_clicked(self):
        self.startScrapingThread = threading.Thread(target=self.startScraping)
        self.startScrapingThread.start()
        # Disable search button
        ui_text = QCoreApplication.translate("MainWindow", u"Start searching...", None)
        self.ui.searchButton.setText(ui_text)
        self.append_label_inline_text(self.ui.messagesLabel, ui_text)
        self.ui.searchButton.setEnabled(False)
        self.ui.stopScrapingButton.setEnabled(True)

    def on_stopScrapingButton_clicked(self):
        stopScrapingThread = threading.Thread(target=self.stopScraping)
        stopScrapingThread.start()
        ui_text = QCoreApplication.translate("MainWindow", u"Stopping Search...", None)
        self.ui.stopScrapingButton.setText(ui_text)
        self.append_label_inline_text(self.ui.messagesLabel, ui_text)
        self.ui.stopScrapingButton.setEnabled(False)
        self.ui.searchButton.setText(self.startButtonText)

    def startScraping(self):
        self.driver_manipulator = DriverManipulator()
        self.googlemapssite = Site(self.driver_manipulator, self.ui.tableWidget)
        self.googlemapssite.scrape_site(self.ui.searchEdit.text())
        self.driver_manipulator.quit_driver()
        # Quit the second driver(edge)
        self.googlemapssite.manipulator.quit_driver()
        # Change buttons states and texts
        self.ui.stopScrapingButton.setEnabled(False)
        self.ui.searchButton.setEnabled(True)
        self.append_label_inline_text(self.ui.messagesLabel,
                                      QCoreApplication.translate("MainWindow", u"Searching is stopped", None))
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
        if self.ui.searchEdit.text():
            self.on_searchButton_clicked()

    def append_label_inline_text(self, qLabel, text):
        # If the label is already have a text
        # then append the text to the next line!
        if qLabel.text():
            qLabel.setText(f"{qLabel.text()}\n{text}")
        else:
            qLabel.setText(text)

    def change_language(self, lang_code):
        """ Change the application language dynamically """
        translation_file = f"translation/translations_{lang_code}.qm"
        if lang_code == "en":
            # Reset to original English texts by removing the translator
            QApplication.instance().removeTranslator(self.translator)
        else:
            if self.translator.load(translation_file):
                QApplication.instance().installTranslator(self.translator)
                print(f"Language changed to {lang_code}")
        self.ui.retranslateUi(self)

    def display_help_dialog(self):
        dialog = dialog_about()
        dialog.exec()

# Run Application
app = QApplication(sys.argv)

# Load system language automatically
translator = QTranslator()
locale = QLocale.system().name()[:2]  # Get system language (e.g., "fr" for French)
locale = "ar"
"""if translator.load(f"translation/translations_{locale}.qm"):
    app.installTranslator(translator)"""

window = WindowApp()
window.show()
sys.exit(app.exec())