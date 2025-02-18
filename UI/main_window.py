import csv
import os
import sys
import threading
import time

from UI.dialog_about import dialog_about
from Ui_MainWindow import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PySide6.QtCore import QTranslator, QLocale, QCoreApplication
from drivermanipulator import DriverManipulator
from wsite import Site
from PySide6.QtWidgets import QTableWidgetItem
from constants import *

class WindowApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.driver_manipulator = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.table_widget = self.ui.tableWidget
        if self.table_widget:
            self.table_widget.setRowCount(TABLE_WIDGET_SIZE)
        self.ui.searchButton.clicked.connect(self.on_searchButton_clicked)
        self.ui.stopScrapingButton.clicked.connect(self.on_stopScrapingButton_clicked)
        self.ui.searchEdit.textChanged.connect(self.on_searchEdit_changed)
        self.ui.listNameEdit.textChanged.connect(self.on_listNameEdit_changed)
        self.ui.searchEdit.returnPressed.connect(self.on_searchEdit_returnPressed)
        # Menu Actions
        self.translator = QTranslator()

        # Connect menu actions to functions
        self.ui.actionEnglish.triggered.connect(lambda: self.change_language("en"))
        self.ui.actionFrench.triggered.connect(lambda: self.change_language("fr"))
        self.ui.actionArabic.triggered.connect(lambda: self.change_language("ar"))        # Disable Stop scraping button
        self.ui.actionAbout.triggered.connect(lambda: self.display_help_dialog())
        self.ui.searchMenuButton.clicked.connect(self.dislpay_search_page)
        self.ui.readButton.clicked.connect(self.dislpay_read_page)
        self.ui.settingsButton.clicked.connect(self.dislpay_settings_page)
        self.ui.saveListButton.clicked.connect(lambda: self.save_list())
        self.ui.searchButton.setEnabled(False)
        self.ui.stopScrapingButton.setEnabled(False)
        # Insert a text inside a edit search
        #self.ui.searchEdit.setText("Plomberie à Reghaia")
        self.stopButtonText = self.ui.stopScrapingButton.text()
        self.startButtonText = self.ui.searchButton.text()
        self.listNameEditChanged = False
        self.searchEditChanged = False
        self.is_start_searching = False
        self.translate_UI()
        # Declare variables
        self.data_buffer = [["Name", "Address", "Phone", "Website", "Maps"]]
        self.__total_places = 0

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
        # Clear and disable buttons and widgets states
        self.is_start_searching = True
        self.table_widget.clearContents()
        self.ui.saveListButton.setEnabled(False)
        self.ui.searchEdit.setEnabled(False)
        self.ui.listNameEdit.setEnabled(False)
        self.driver_manipulator = DriverManipulator()
        self.googlemapssite = Site(self.driver_manipulator, self)
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
        self.ui.searchEdit.setEnabled(True)
        self.ui.listNameEdit.setEnabled(True)
        self.is_start_searching = False
        self.__total_places = 0

    def stopScraping(self):
        self.googlemapssite.stop_scraping()
        # Quit first and second drivers
        time.sleep(2)

    def on_searchEdit_changed(self, newText):
        if not newText:
            self.searchEditChanged = False
            self.ui.searchButton.setEnabled(False)
            return
        self.searchEditChanged = True
        if self.listNameEditChanged and newText and not self.is_start_searching:
            self.ui.searchButton.setEnabled(True)

    def on_listNameEdit_changed(self, newText):
        if not newText:
            self.listNameEditChanged = False
            self.ui.searchButton.setEnabled(False)
            return
        self.listNameEditChanged = True
        if self.searchEditChanged and not self.is_start_searching:
            self.ui.searchButton.setEnabled(True)
            # Set the project name
        PROJECT_CONFIG["name"] = self.ui.listNameEdit.text()
        print("PROJECT_CONFIG[name]" + PROJECT_CONFIG["name"])


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

    def dislpay_search_page(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def dislpay_read_page(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def dislpay_settings_page(self):
        self.ui.stackedWidget.setCurrentIndex(2)


    def update_table_widget(self):
        # Get data from scraping logic
        data = self.googlemapssite.pass_data_to_UI()
        self.scraped_data = data["scraped_data"]
        for col, value in enumerate(self.scraped_data):
            item = QTableWidgetItem(value)
            self.table_widget.setItem(self.__total_places, col, item)
        self.__total_places += 1
        print(f"total_places: {self.__total_places}")
        # Enable save list button
        self.ui.saveListButton.setEnabled(True)
        # Append data to buffer
        self.data_buffer.append(self.scraped_data)

    """def clear_table_widget(self):
        for i in range(self.__total_places):
            for col, value in enumerate(self.scraped_data):
                self.table_widget.setItem(self.__total_places, col, None)"""

    def get_download_directory(self):
        # Get the user's profile directory
        user_profile = os.getenv('USERPROFILE')

        if user_profile:
            # Construct the path to the Downloads directory
            download_directory = os.path.join(user_profile, 'Downloads')
            return download_directory
        else:
            raise EnvironmentError("Unable to determine the user's profile directory.")

    def save_list(self):
        # Open a file save dialog
        file_path, filter = QFileDialog.getSaveFileName(
            self,  # Parent window
            "Save List File",  # Dialog title
            "/".join((self.get_download_directory(), self.ui.searchEdit.text())),  # Default directory (empty for current directory)
            "CSV Files (*.csv);;Text Files (*.txt)All Files (*)"  # File filters
        )
        # Save the buffer content to a CSV file

        if file_path:
            try:
                with open(file_path, mode="w", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerows(self.data_buffer)
                    QMessageBox.information(self, self.tr("Success"), self.tr("File saved successfully!"))

            except Exception as e:
                QMessageBox.critical(self, self.tr("Error"), self.tr(f"Failed to save file: {str(e)})"))

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