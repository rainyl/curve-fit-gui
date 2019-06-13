# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/run/media/rainy/DEV/python/pyqt/project/curve-fit-gui/res/UI/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import (QMainWindow, QGridLayout, QWidget, QMenuBar, QMenu,
                             QStatusBar, QAction, QVBoxLayout, QFormLayout,
                             QHBoxLayout, QLabel, QCheckBox, QDoubleSpinBox,
                             QPushButton, QFileDialog)
from PyQt5.QtCore import (QRect, QMetaObject, QRegExp, QCoreApplication)
from PyQt5.QtGui import QRegExpValidator, QIcon, QPainter, QColor
import res.res
from src.slots.MainWindow import *
from src.utils.SSSetter import *
from src.config import *
# from PyQt5.QtWebEngineWidgets import QWebEngineView

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(Skin.get_qss())
        self.filter = "csv or xls(*.csv *.xls *.xlsx)"
        self.regValidator = QRegExpValidator(QRegExp('[0-9]{0,10}\.{0,1}[0-9]{0,3}'), self)

    def setupUI(self):
        self.setupBar()
        self.setupContent()
        self.retranslateUi()
        self.setupGlobal()
        self.setupDialog()

    def setupGlobal(self):
        # self.setObjectName("MainWindow")
        # self.resize(800, 600)
        # self.setStyleSheet("")
        layout = QGridLayout()
        layout.addLayout(self.vbxlot_left, 0, 0)
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 3)
        layout.addLayout(self.vbxlot_right, 0, 1)
        self.setGeometry(QRect(200, 200, 1100, 600))
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setLayout(layout)
        self.setCentralWidget(self.centralwidget)
        QMetaObject.connectSlotsByName(self)
        self.setWindowIcon(QIcon(":/images/icon"))
        # self.setLayout(layout)

    def setupBar(self):
        self.menubar = QMenuBar(self)
        self.menubar.setStyleSheet(getMenuQSS("#3498DB", "#FFFFFF", "#2483C7", "#A0DAFB"))
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menuFiles = QMenu(self.menubar)
        self.menuFiles.setObjectName("menuFiles")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menu = QMenu(self.menuAbout)
        self.menu.setObjectName("menu")
        self.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(self)
        self.statusBar.setObjectName("statusBar")
        self.setStatusBar(self.statusBar)
        # self.actionNew = QAction(self)
        # self.actionNew.setObjectName("actionNew")
        # self.actionOpen = QAction(self)
        # self.actionOpen.setObjectName("actionOpen")
        # self.actionSave = QAction(self)
        # self.actionSave.setObjectName("actionSave")
        self.actionSaveAs = QAction(self)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionAuthor = QAction(self)
        self.actionAuthor.setObjectName("actionAuthor")
        self.actionTutorial = QAction(self)
        self.actionTutorial.setObjectName("actionTutorial")
        self.actionGithub = QAction(self)
        self.actionGithub.setObjectName("actionGithub")
        self.actionExit = QAction(self)
        self.actionExit.setObjectName("actionExit")
        # self.menuFiles.addAction(self.actionNew)
        # self.menuFiles.addAction(self.actionOpen)
        # self.menuFiles.addAction(self.actionSave)
        self.menuFiles.addAction(self.actionSaveAs)
        self.menuFiles.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionTutorial)
        self.menu.addAction(self.actionAuthor)
        self.menuAbout.addAction(self.menu.menuAction())
        self.menuAbout.addAction(self.actionGithub)
        self.menubar.addAction(self.menuFiles.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())


    def setupContent(self):
        # vbxlot = vboxlayout
        # hbxlot = hboxlayout
        # fmlot = formlayout
        # lbl = label
        # ledt = lineedit
        self.vbxlot_left = QVBoxLayout()
        self.vbxlot_right = QVBoxLayout()
        self.fmlot_args = QFormLayout()

        # left
        # 标签
        self.lbl_arg_ave = QLabel("Ave")
        # lbl_arg_ave.setStyleSheet("color:rgb(255, 255, 255);")
        self.lbl_arg_Cs = QLabel("Cs")
        # lbl_arg_Cs.setStyleSheet("color:rgb(255, 255, 255);")
        self.lbl_arg_Cv = QLabel("Cv")
        # lbl_arg_Cv.setStyleSheet("color:rgb(255, 255, 255);")
        self.lbl_arg_Fac = QLabel("Fac")

        # 复选框
        self.chkb_extreme_flood = QCheckBox("Extreme Flood")
        #
        # # 单行文本
        # self.ledt_arg_ave = QLineEdit()
        # self.ledt_arg_ave.setValidator(self.regValidator)
        # self.ledt_arg_ave.setStyleSheet(getEditQSS("#DCE4EC", "#1ABC9C"))
        # self.ledt_arg_Cs = QLineEdit()
        # self.ledt_arg_Cs.setDisabled(True)
        # self.ledt_arg_Cs.setValidator(self.regValidator)
        # self.ledt_arg_Cs.setStyleSheet(getEditQSS("#DCE4EC", "#3498DB"))
        # self.ledt_arg_Cv = QLineEdit()
        # self.ledt_arg_Cv.setValidator(self.regValidator)
        # self.ledt_arg_Cv.setStyleSheet(getEditQSS("#DCE4EC", "#E74C3C"))
        # self.ledt_arg_Fac = QLineEdit()
        # self.ledt_arg_Fac.setValidator(QRegExpValidator(QRegExp('[0-9]{1}\.{0,1}[0-9]{0,3}')))
        # # self.ledt_arg_Fac.setValidator(QDoubleValidator(0, 9, 3, self))
        # self.ledt_arg_Fac.setStyleSheet(getEditQSS("#DCE4EC", "#E74C3C"))

        # spinbox
        self.spbx_ave = QDoubleSpinBox()
        self.spbx_ave.setPrefix('ave: ')
        self.spbx_ave.setSingleStep(0.01)
        self.spbx_ave.setRange(0, 999999)
        self.spbx_ave.setObjectName(Namer.spbx_ave)
        self.spbx_cv = QDoubleSpinBox()
        self.spbx_cv.setPrefix("Cv:  ")
        self.spbx_cv.setSingleStep(0.01)
        self.spbx_cv.setRange(0, 999999)
        self.spbx_cv.setObjectName(Namer.spbx_cv)
        self.spbx_fac = QDoubleSpinBox()
        self.spbx_fac.setPrefix("Fac: ")
        self.spbx_fac.setSingleStep(0.01)
        self.spbx_fac.setRange(0, 999999)
        self.spbx_fac.setObjectName(Namer.spbx_fac)
        self.spbx_cs = QDoubleSpinBox()
        self.spbx_cs.setPrefix("Cs:  ")
        self.spbx_cs.setSingleStep(0.01)
        self.spbx_cs.setRange(0, 999999)
        self.spbx_cs.setObjectName(Namer.spbx_cs)
        self.spbx_cs.setDisabled(True)


        #
        # # 滑块
        # self.sld_arg_ave = QSlider(Qt.Horizontal)
        # self.sld_arg_ave.setMinimum(0)
        # self.sld_arg_ave.setMaximum(100)
        # self.sld_arg_ave.setStyleSheet(getSilderQSS("#E8EDF2", "#1ABC9C", "#1ABC9C"))
        #
        # self.sld_arg_Cs = QSlider(Qt.Horizontal)
        # self.sld_arg_Cs.setStyleSheet(getSilderQSS("#E8EDF2", "#3498DB", "#3498DB"))
        #
        # self.sld_arg_Cv = QSlider(Qt.Horizontal)
        # self.sld_arg_Cv.setMinimum(0)
        # self.sld_arg_Cv.setMaximum(100)
        # self.sld_arg_Cv.setStyleSheet(getSilderQSS("#E8EDF2", "#E74C3C", "#E74C3C"))
        #
        # self.sld_arg_Fac = QSlider(Qt.Horizontal)
        # self.sld_arg_Fac.setMinimum(0)
        # self.sld_arg_Fac.setMinimum(100)
        # self.sld_arg_Fac.setStyleSheet(getSilderQSS("#E8EDF2", "#E74C3C", "#E74C3C"))

        # 表单容器
        self.fmlot_args.addRow(self.spbx_ave)
        self.fmlot_args.addRow(self.spbx_cv)
        self.fmlot_args.addRow(self.spbx_fac)
        self.fmlot_args.addRow(self.spbx_cs)
        # self.fmlot_args.addRow(self.lbl_arg_ave, self.ledt_arg_ave)
        # self.fmlot_args.addRow(self.sld_arg_ave)
        # self.fmlot_args.addRow(self.lbl_arg_Cv, self.ledt_arg_Cv)
        # self.fmlot_args.addRow(self.sld_arg_Cv)
        # self.fmlot_args.addRow(self.lbl_arg_Fac, self.ledt_arg_Fac)
        # self.fmlot_args.addRow(self.sld_arg_Fac)
        # self.fmlot_args.addRow(self.lbl_arg_Cs, self.ledt_arg_Cs)
        # self.fmlot_args.addRow(self.sld_arg_Cs)
        # self.fmlot_args.addRow(self.chkb_extreme_flood)

        # 按钮
        self.btn_import = QPushButton("&Import")
        self.btn_import.setObjectName(Namer.btn_import)
        self.btn_import.setStyleSheet(getButtonQSS("#34495E", "#FFFFFF", "#4E6D8C", "#F0F0F0", "#2D3E50", "#B8C6D1"))
        self.btn_export = QPushButton("&Export")
        self.btn_export.setObjectName(Namer.btn_export)
        self.btn_export.setStyleSheet(getButtonQSS("#1ABC9C", "#E6F8F5", "#2EE1C1", "#FFFFFF", "#16A086", "#A7EEE6"))

        self.hbxlot_left = QHBoxLayout()
        self.hbxlot_left.addWidget(self.btn_import)
        self.hbxlot_left.addWidget(self.btn_export)

        self.vbxlot_left.addLayout(self.fmlot_args)
        self.vbxlot_left.addLayout(self.hbxlot_left)

        # right
        # 图像
        # self.lbl_curve = QLabel()
        # self.lbl_curve.setAutoFillBackground(True)
        # self.lbl_curve.setStyleSheet("QLabel { background-color :rgba(0, 0, 0, 0.5);color:rgb(255, 255, 255);}")
        # self.lbl_curve.setPixmap(
        #     QPixmap(":/images/background").scaled(self.lbl_curve.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

        # self.browser = QWebEngineView()
        # self.browser.load(QUrl('file:///run/media/rainy/DEV/python/pyqt/project/curve-fit-gui/render.html'))

        self.fig = Figure()
        self.canvas = FigureCanvas(self.fig)
        ax = self.fig.add_subplot(111)
        ax.set_title('curve')

        # 按钮
        self.btn_go = QPushButton('&Go')
        self.btn_go.setObjectName(Namer.btn_go)
        self.btn_go.setStyleSheet(getButtonQSS("#00CED1", "#FFFFFF", "#AFEEEE", "#FFFFFF", "#00CED1", "#A0DAFB"))
        self.btn_show_data = QPushButton("&Show data")
        self.btn_show_data.setObjectName(Namer.btn_show_data)
        self.btn_show_data.setStyleSheet(getButtonQSS("#3498DB", "#FFFFFF", "#5DACE4", "#E5FEFF", "#2483C7", "#A0DAFB"))
        self.btn_save_as = QPushButton("&Save As")
        self.btn_save_as.setObjectName(Namer.btn_save_as)
        self.btn_save_as.setStyleSheet(getButtonQSS("#3498DB", "#FFFFFF", "#5DACE4", "#E5FEFF", "#2483C7", "#A0DAFB"))
        self.btn_clear = QPushButton("&Clear")
        self.btn_clear.setObjectName(Namer.btn_clear)
        self.btn_clear.setStyleSheet(getButtonQSS("#E74C3C", "#FFFFFF", "#EC7064", "#FFF5E7", "#DC2D1A", "#F5A996"))
        self.btn_exit = QPushButton("&Exit")
        self.btn_exit.setObjectName(Namer.btn_exit)
        self.btn_exit.setStyleSheet(getButtonQSS("#E74C3C", "#FFFFFF", "#EC7064", "#FFF5E7", "#DC2D1A", "#F5A996"))

        self.hbxlot_right = QHBoxLayout()
        self.hbxlot_right.addWidget(self.btn_go)
        self.hbxlot_right.addWidget(self.btn_show_data)
        self.hbxlot_right.addWidget(self.btn_save_as)
        self.hbxlot_right.addWidget(self.btn_clear)
        self.hbxlot_right.addWidget(self.btn_exit)

        # self.vbxlot_right.addWidget(self.lbl_curve)
        # self.vbxlot_right.addWidget(self.browser)
        self.vbxlot_right.addWidget(self.canvas)
        self.vbxlot_right.addLayout(self.hbxlot_right)

        # 重绘界面
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor(255, 255, 255))

    # 翻译界面
    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "主界面"))
        self.menuFiles.setTitle(_translate("MainWindow", "文件"))
        self.menuEdit.setTitle(_translate("MainWindow", "编辑"))
        self.menuHelp.setTitle(_translate("MainWindow", "帮助"))
        self.menuAbout.setTitle(_translate("MainWindow", "关于"))
        self.menu.setTitle(_translate("MainWindow", "关于本软件"))
        # self.actionNew.setText(_translate("MainWindow", "新建"))
        # self.actionOpen.setText(_translate("MainWindow", "打开"))
        # self.actionSave.setText(_translate("MainWindow", "保存"))
        self.actionSaveAs.setText(_translate("MainWindow", "另存为"))
        self.actionAuthor.setText(_translate("MainWindow", "作者"))
        self.actionTutorial.setText(_translate("MainWindow", "使用教程"))
        self.actionGithub.setText(_translate("MainWindow", "Github"))
        self.actionExit.setText(_translate("MainWindow", "退出"))

        self.btn_import.setText(_translate("MainWindow", "导入"))
        self.btn_export.setText(_translate("MainWindow", "导出"))
        self.btn_show_data.setText(_translate("MainWindow", "显示数据"))
        self.btn_go.setText(_translate("MainWindow", "走你"))
        self.btn_save_as.setText(_translate("MainWindow", "另存为"))
        self.btn_clear.setText(_translate("MainWindow", "清除"))
        self.btn_exit.setText(_translate("MainWindow", "退出"))

        # self.ledt_arg_ave.setText(_translate("MainWindow", "请输入数字"))
        # self.ledt_arg_Cv.setText(_translate("MainWindow", "请输入数字"))
        # self.ledt_arg_Fac.setText(_translate("MainWindow", "请输入不大于10的小数"))
        # self.ledt_arg_Cs.setText(_translate("MainWindow", "不可输入"))

        self.chkb_extreme_flood.setText(_translate("MainWindow", "特大洪水"))

    def setupDialog(self):
        self.fileDialog = QFileDialog()
        self.fileDialog.setStyleSheet(getDialogQSS("#FFFFFF"))

