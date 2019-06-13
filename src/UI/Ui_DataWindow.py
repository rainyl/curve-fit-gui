from PyQt5.QtWidgets import QTableWidget, QWidget, QHBoxLayout, QTableWidgetItem
from src.utils.SSSetter import *
from PyQt5.QtCore import QRect


class Ui_DataWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Data')
        self.setStyleSheet("background-color: #FFFFFF;")
        self.setGeometry(QRect(200, 200, 800, 600))
        self.setupUi()

    def setupUi(self):
        self.table_left = QTableWidget()
        self.table_left.setColumnCount(2)
        self.table_left.setWindowTitle("原始量")
        self.table_left.setHorizontalHeaderLabels(['P(%)', 'Q(m3/s)'])

        self.table_right = QTableWidget()
        self.table_right.setColumnCount(2)
        self.table_right.setHorizontalHeaderLabels(['P(%)', 'Q(m3/s)'])

        layout = QHBoxLayout()
        layout.addWidget(self.table_left)
        layout.addWidget(self.table_right)

        self.setLayout(layout)

    # 设置text，widget指定widget, data=[[], [], []]
    def setText(self, data, widget='left'):
        rows = len(data)
        columns = 2
        if widget == 'left':
            self.table_left.clearContents()
            self.table_left.setHorizontalHeaderLabels(['P(%)', 'Q(m3/s)'])
            self.table_left.setRowCount(rows)
            for r, row in enumerate(data):
                self.table_left.setItem(r, 0, QTableWidgetItem(str(round(row[0]*100, 2))))
                self.table_left.setItem(r, 1, QTableWidgetItem(str(round(row[1], 2))))
        elif widget == 'right':
            self.table_right.clearContents()
            self.table_right.setHorizontalHeaderLabels(['P(%)', 'Q(m3/s)'])
            self.table_right.setRowCount(rows)
            for r, row in enumerate(data):
                self.table_right.setItem(r, 0, QTableWidgetItem(str(round(row[0], 2))))
                self.table_right.setItem(r, 1, QTableWidgetItem(str(round(row[1], 2))))
        else:
            return False
