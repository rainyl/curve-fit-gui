from PyQt5.QtWidgets import QWidget, QTextEdit, QHBoxLayout
from src.utils.SSSetter import *
from PyQt5.QtCore import QRect, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from src.config import *


class Ui_HelpWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Help')
        self.setGeometry(QRect(200, 200, 800, 600))
        self.setupUi()

    def setupUi(self):
        self.browser = QWebEngineView()
        self.browser.load(QUrl('https://github.com/rainyl/curve-fit-gui/blob/master/README.md'))
        layout = QHBoxLayout()
        layout.addWidget(self.browser)

        self.setLayout(layout)

    def getDoc(self):
        with open(HELP_HTML_PATH) as f:
            data = f.read()
        return data

