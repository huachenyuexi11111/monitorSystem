import sys
from monitor.monitorapp import MonitorApp
if __name__ == '__main__':
    # 创建并运行监控应用程序
    app = MonitorApp()
    sys.exit(app.exec())