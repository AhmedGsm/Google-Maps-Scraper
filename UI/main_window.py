import sys
from Ui_MainWindow import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow

class WindowApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

myApp = QApplication(sys.argv)
window = WindowApp()
window.show()
myApp.exit(myApp.exec())