#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.slots.MainWindow import MainWindow
from PyQt5.QtWidgets import QApplication
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
