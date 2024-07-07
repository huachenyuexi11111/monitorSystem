from PyQt5 import QtWidgets, QtGui, QtCore
from monitor.loginui import Ui_Dialog
from monitor.mainframe import MainDialog

class LoginDialog(QtWidgets.QMainWindow):
    """
    登录对话框类，提供用户登录功能。
    """
    def __init__(self):
        super().__init__()
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

        # 绑定登录按钮点击事件
        self.ui.pushButton.clicked.connect(self.login_button_clicked)

    def on_resize(self, event):
        # 当窗口大小发生变化时，调整标签的大小并重新设置其显示的图像
        self.label.resize(self.width(), self.height())
        self.label.setPixmap(self.pixmap.scaled(self.label.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio,
                                                transformMode=QtCore.Qt.SmoothTransformation))

    def login_button_clicked(self):
        # 获取用户名和密码
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        # 验证用户名和密码
        if username == "admin" and password == "password":
            self.mainframe = MainDialog()
            self.mainframe.show()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "登录失败", "用户名或密码错误！")

