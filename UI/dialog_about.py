from PySide6.QtWidgets import QDialog

from UI.Ui_DialogAbout import Ui_Dialog


class dialog_about(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonOk.clicked.connect(self.close)
