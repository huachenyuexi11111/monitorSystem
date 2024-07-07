from PyQt5.QtWidgets import QApplication
from monitor.mainframe import MainDialog
from monitor.login import LoginDialog
import sys

class MonitorApp(QApplication):
    def __init__(self):
        super(MonitorApp, self).__init__(sys.argv)
        self.dialog = LoginDialog()
        # 显示登陆界面
        self.dialog.show()