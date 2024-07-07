from monitor.mfuip import Ui_Dialog_3
from PyQt5 import QtCore
from PyQt5.Qt import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtWidgets, QtGui, QtCore
from monitor.VideoPeople import VideoPeople

class MonitorPDialog(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.running = True
        self.label = QtWidgets.QLabel(self)
        self.setCentralWidget(self.label)
        self.pixmap = QtGui.QPixmap("data/sysbg.jpg")
        # 设置QLabel的尺寸
        self.label.resize(self.width(), self.height())
        self.label.setScaledContents(True)
        # 将背景图片设置为QLabel的内容
        self.label.setPixmap(self.pixmap.scaled(self.label.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio,
                                                transformMode=QtCore.Qt.SmoothTransformation))
        # 监听窗口大小变化事件
        self.resizeEvent = self.on_resize

        self.ui = Ui_Dialog_3()
        self.ui.setupUi(self)
        self.ui.label_11.setStyleSheet("background-image: url('data/white.png');")
        self.ui.label_12.setStyleSheet("background-image: url('data/white.png');")

        self.th1 = VideoPeople('data/vd1.mp4')
        # 绑定信号与槽函数
        self.th1.send.connect(self.showimg)
        self.th1.start()

        self.th2 = VideoPeople('data/vd2.mp4')
        # 绑定信号与槽函数
        self.th2.send.connect(self.showimg)
        self.th2.start()

        # 在窗口大小发生变化时调整一个标签 (label) 的大小，并重新设置其显示的图像

    def on_resize(self, event):
        self.label.resize(self.width(), self.height())
        self.label.setPixmap(self.pixmap.scaled(self.label.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio,
                                                transformMode=QtCore.Qt.SmoothTransformation))

    def showimg(self, h, w, c, b, th_id, num, dev):
        '''
        在标签上显示视频帧图像。

        :param h:图像高度。
        :param w:图像宽度。
        :param c:图像通道数。
        :param b:图像字节数据。
        :param th_id:线程ID。
        :param num:检测到的人数。
        :return:无
        '''
        # QImage.Format_BGR888：R G B
        imgae = QImage(b, w, h, w * c, QImage.Format_BGR888)
        pix = QPixmap.fromImage(imgae)
        self.dev = dev
        if th_id == 1:
            # 自动缩放
            width = self.ui.label.width()
            height = self.ui.label.height()
            scale_pix = pix.scaled(width, height, Qt.KeepAspectRatio)
            self.ui.label.setPixmap(scale_pix)
            # str(num) 类型转换
            self.ui.label_8.setText(str(num))
        elif th_id == 2:
            # 自动缩放
            width = self.ui.label_2.width()
            height = self.ui.label_2.height()
            scale_pix = pix.scaled(width, height, Qt.KeepAspectRatio)
            self.ui.label_2.setPixmap(scale_pix)
        if num > 10:

            self.ui.label_9.setText('<span style="color: red;">拥挤</span>')
        else:
            self.ui.label_9.setText('<span style="color: green;">畅通</span>')

    def ReturnChoose_2(self):
        '''
        返回监控对象选择界面
        :return: 无
        '''
        from monitor.mainframe import MainDialog
        self.dev.release()
        self.th1.stop()
        self.th2.stop()
        self.close()
        self.mainframe = MainDialog()
        self.mainframe.show()

    def SwitchCar(self):
        '''
        转换到车辆监控界面
        :return: 无
        '''
        from monitor.monitorframe import MonitorDialog
        self.dev.release()
        self.th1.stop()
        self.th2.stop()
        self.close()
        self.monitorframe = MonitorDialog()
        self.monitorframe.show()