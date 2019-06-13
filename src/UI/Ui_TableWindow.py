from PyQt5.QtWidgets import QWidget, QTableView, QVBoxLayout
from src.utils.SSSetter import *
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtSql import QSqlTableModel


class Ui_Table_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setupGlobal()
        self.setupUtils()
        self.setupContent()

    def setupGlobal(self):
        self.setWindowTitle('Data Table')
        self.setGeometry(QRect(200, 200, 800, 600))

    def setupUtils(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('flood')
        self.model.setSort(0, Qt.AscendingOrder)
        self.model.setHeaderData(0, Qt.Horizontal, 'ID')
        self.model.setHeaderData(1, Qt.Horizontal, 'Year')
        self.model.setHeaderData(2, Qt.Horizontal, 'Q')
        self.model.select()

    def setupContent(self):
        self.viewUp = QTableView()
        self.viewUp.setModel(self.model)
        self.viewUp.setSelectionMode(QTableView.SingleSelection)
        self.viewUp.setSelectionBehavior(QTableView.SelectRows)
        self.viewUp.resizeColumnsToContents()

        self.viewDown = QTableView()
        self.viewDown.setModel(self.model)
        self.viewDown.setSelectionMode(QTableView.SingleSelection)
        self.viewDown.setSelectionBehavior(QTableView.SelectRows)
        self.viewDown.resizeColumnsToContents()

        layout = QVBoxLayout()
        layout.addWidget(self.viewUp)
        layout.addWidget(self.viewDown)

        self.setLayout(layout)
