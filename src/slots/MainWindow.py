from src.UI.Ui_MainWindow import Ui_MainWindow
from src.UI.Ui_TableWindow import Ui_Table_Window
from src.UI.Ui_DataWindow import Ui_DataWindow
from src.UI.Ui_HelpWindow import Ui_HelpWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from src.utils.SSSetter import getDialogQSS
from src.utils.DataReader import DataReader
from src.utils.DataSaver import DataSaver
from src.utils.ploter import Ploter
from src.P3.flood import ExtrameFlood, Flood
from src.config import *
import sys
import logging
import webbrowser


class MainWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.setup_windows()
        self.setup_slot()
        self.setup_logging()
        self.setup_utils()
        self.flood_args = FLOOD_ARGS  # 计算的参数，格纸为字典，见config对应值示例
        self.data_ori = ''  # 初始导入数据
        self.flooder = None
        self.extreme_flood = False

    # 初始化设置工具
    def setup_utils(self):
        # self.db = DatabaseFlood(db_name='Flood.db')  # 数据库
        self.msgBox = QMessageBox(self)  # 实例化messagebox， 用于弹出提示框
        self.msgBox.setIconPixmap(QPixmap(":/images/warning"))
        self.msgBox.setStyleSheet(getDialogQSS("#FFFFFF"))  # 设置提示框样式表
        self.img = QImage()  # 实例化QIMAGE对象
        self.ploter = Ploter()

    # 初始化设置页面
    def setup_windows(self):
        self.table_window = Ui_Table_Window()  # 实例化表格页面对象
        self.data_window = Ui_DataWindow()  # 实例化数据页面对象
        self.help_window = Ui_HelpWindow()  # 实例化帮助页面对象

    # 设置日志记录工具
    def setup_logging(self):
        logging.basicConfig(level=logging.DEBUG)

    # 设置信号槽
    def setup_slot(self):
        # event for button
        self.btn_import.clicked.connect(self.btn_import_clicked)  # 导入数据
        self.btn_export.clicked.connect(self.btn_export_clicked)  # 导出数据
        self.btn_clear.clicked.connect(self.btn_clear_clicked)  # 清除图像
        self.btn_go.clicked.connect(self.btn_go_clicked)  # 执行计算
        self.btn_save_as.clicked.connect(self.btn_save_as_clicked)  # 将图像另存为
        self.btn_exit.clicked.connect(self.btn_exit_clicked)  # 退出
        self.btn_show_data.clicked.connect(self.btn_show_data_clicked)  # 显示数据

        self.spbx_ave.editingFinished.connect(self.on_spbx_edit_finished)
        self.spbx_cv.editingFinished.connect(self.on_spbx_edit_finished)
        self.spbx_fac.editingFinished.connect(self.on_spbx_edit_finished)

        # for check box
        # self.chkb_extreme_flood.stateChanged.connect(self.chkb_extreme_flood_state_changed)

        # for menubar
        self.actionTutorial.triggered.connect(self.action_tutorial_triggered)  # 连接到帮助按钮的信号槽
        self.actionSaveAs.triggered.connect(self.btn_save_as_clicked)
        self.actionGithub.triggered.connect(lambda: webbrowser.open(GITHUB_URL))
        self.actionAuthor.triggered.connect(self.action_tutorial_triggered)
        self.actionExit.triggered.connect(lambda: sys.exit(0))

    # 导入按钮信号槽
    def btn_import_clicked(self, event):
        logging.debug("[MAINWINDOW]import pressed")
        # TODO 导入数据到其他函数进行计算
        open_file_name = self.fileDialog.getOpenFileName(self, '.', filter="csv or xls(*.csv *.xls *.xlsx)")
        try:
            data = DataReader.read(open_file_name[0])
            if data is None:
                self.msgBox.setWindowTitle('INFO')
                self.msgBox.setText("open file error!")
                self.msgBox.show()
            else:
                self.data_ori = data
                self.flood_args[Namer.flood_data] = data[:, 1]
                self.flooder = Flood.Flood(self.flood_args)
                self.flood_args[Namer.spbx_ave] = self.flooder.ave
                self.flood_args[Namer.spbx_cv] = self.flooder.Cv
                self.flood_args[Namer.spbx_cs] = self.flooder.Cs
                self.refresh()
                # self.set_spbx_value()
                self.btn_go.setEnabled(True)
            # TODO 存储到数据库
            # else:
            #     result = self.db.saveTo(data, 'flood')
            #     if result != DB.DB_SUCCEED:
            #         QMessageBox.warning(self, 'database error', result)

        except Exception as e:
            logging.warning("[MAINWINDOW]"+str(e))

    def btn_export_clicked(self, event):
        logging.debug("[MAINWINDOW] export pressed")
        try:
            data = [[x, y] for x, y in zip(self.flooder.x_std, self.flooder.y)]
            if len(data) == 0:
                self.msgbox.setWindowTitle('ERROR')
                self.msgbox.setText('Data is Empty!')
                self.msgbox.show()
            else:
                save_file_name = self.fileDialog.getSaveFileName(self, '.', filter="csv or xls file(*.csv *.xls *.xlsx)")
                DataSaver.save(save_file_name[0], data)
        except Exception as e:
            logging.error("[MAINWINDOW] " + str(e))
            self.msgbox.setWindowTitle('ERROR')
            self.msgbox.setText('Save Error!')
            self.msgbox.show()
        # TODO 添加导出函数，pandas，利用其它函数

    # Go按钮用于执行计算
    def btn_go_clicked(self):
        logging.debug('[MAINWINDOW] go btn pressed')
        if len(self.data_ori) == 0:
            QMessageBox.warning(self, "Warning", 'Please import data first!')
        else:
            self.refresh()
            self.btn_go.setDisabled(True)

    # 跳转到data界面
    def btn_show_data_clicked(self, event):
        try:
            data = [[x, y] for x, y in zip(self.flooder.p, self.flooder.y_ori)]
            self.data_window.setText(data, 'left')
            data = [[x, y] for x, y in zip(self.flooder.x_std, self.flooder.y)]
            self.data_window.setText(data, 'right')
        except Exception as e:
            logging.warning(e)
        self.data_window.show()

    def btn_save_as_clicked(self, event):
        logging.debug('[MAINWINDOW] save as pressed')
        save_file_name = self.fileDialog.getSaveFileName(self, '.', filter="png images(*.png)")
        try:
            self.canvas.print_png(save_file_name[0])
        except Exception as e:
            logging.warning(e)

    def btn_clear_clicked(self):
        logging.debug('[MAINWINDOW] clear pressed')
        self.fig.clear(True)
        ax = self.fig.add_subplot(111)
        ax.set_title('curve')
        self.canvas.draw()

    def btn_exit_clicked(self):
        sys.exit(0)

    def chkb_extreme_flood_state_changed(self, event):
        if event == Qt.Checked:
            self.extreme_flood = True
            logging.debug("[MAINWINDOW] 特大洪水模式")
            self.flooder = ExtrameFlood.ExtremeFlood()
        else:
            self.extreme_flood = False
            logging.debug("[MAINWINDOW] 非特大洪水")
            self.flooder = Flood.Flood()

    def on_spbx_edit_finished(self):
        sender = self.sender()
        try:
            self.flood_args[sender.objectName()] = round(float(sender.value()), 2)
            self.refresh()
        except Exception as e:
            logging.warning("[MAINWINDOW] " + str(e))

    def action_tutorial_triggered(self):
        self.help_window.show()

    def set_spbx_value(self):
        self.spbx_ave.setValue(self.flooder.ave)
        self.spbx_cv.setValue(self.flooder.Cv)
        self.spbx_cs.setValue(self.flooder.Cs)
        self.spbx_fac.setValue(self.flooder.fac)

    def refresh(self):
        self.flooder.refresh(self.flood_args)
        label = "ave=" + str(round(self.flooder.ave, 2)) + "$m^3/s$\nCv=" + str(round(self.flooder.Cv, 2)) + "\nCs=" + str(self.flooder.fac) + "Cv"
        self.plot_(self.flooder.x, self.flooder.y, label=label)
        self.set_spbx_value()

    def plot_(self, x, y, line_style="o--", label="", title="curve"):
        self.fig.clf()
        ax = self.fig.add_subplot(111)
        self.ploter.heisen(ax)
        self.ploter.plot_original_points(ax, y=self.data_ori[:, 1])
        ax.plot(x, y, line_style, label=label)
        ax.set_title(title)
        ax.legend()
        self.canvas.draw()
