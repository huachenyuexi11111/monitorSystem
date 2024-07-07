from PyQt5 import QtWidgets, QtGui, QtCore
from monitor.mdui import Ui_Dialog
from monitor.monitorframe import MonitorDialog
from monitor.monitorpeopleframe import MonitorPDialog

class MainDialog(QtWidgets.QMainWindow):
    """
    主对话框类，提供主窗口功能和监控对象选择。
    """
    def __init__(self):
        super().__init__()
        self.flag = 0
        self.monitorframe = None
        # 创建一个QLabel并设置为主窗口的中央部件
        self.label = QtWidgets.QLabel(self)
        self.setCentralWidget(self.label)
        self.pixmap = QtGui.QPixmap("data/bg.jpg")
        # 设置QLabel的尺寸
        self.label.resize(self.width(), self.height())
        self.label.setScaledContents(True)
        # 将背景图片设置为QLabel的内容
        self.label.setPixmap(self.pixmap.scaled(self.label.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio,
                                                transformMode=QtCore.Qt.SmoothTransformation))

        # 监听窗口大小变化事件
        self.resizeEvent = self.on_resize
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.label_4.setStyleSheet("background-image: url('data/white.png');")


    # 在窗口大小发生变化时调整一个标签 (label) 的大小，并重新设置其显示的图像
    def on_resize(self, event):
        self.label.resize(self.width(), self.height())
        self.label.setPixmap(self.pixmap.scaled(self.label.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio,
                                                transformMode=QtCore.Qt.SmoothTransformation))

    def PeopleMonitor(self):
        # 设置监控标志为2，表示选择了人群监控
        self.flag = 2
        return self.flag


    def CarMonitor(self):
        # 设置监控标志为1，表示选择了车辆监控
        self.flag = 1
        return self.flag


    def goin(self):
        # 根据监控标志打开对应的监控窗口
        if self.flag == 1:
            self.monitorframe = MonitorDialog()
            self.monitorframe.show()
            self.close()
        elif self.flag == 2:
            self.monitorframe = MonitorPDialog()
            self.monitorframe.show()
            self.close()
        elif self.flag == 0:
            self.ui.label_3.setText('<span style="color: red;">请先选择监控对象！</span>')

