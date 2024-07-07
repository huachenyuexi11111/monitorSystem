from PyQt5.QtCore import QThread
import cv2 as cv
from PyQt5.QtCore import pyqtSignal
from ai.car import vehicle_detect
# 重写run()方法: 线程执行的内容
# Thread的实例对象.start()  run()就会自动执行
class Video(QThread):
    # 使用信号与槽槽函数向外传递数据
    #    发送者   Video
    #    信号类型  自定义信号类型(参数信号所能传递的数据)
    #    接收者   （线程所在的Dialog）
    #    槽函数   （接收者类：功能方法）
    send = pyqtSignal(int, int, int, bytes, int, int, object) #emit
    def __init__(self,video_id):
        super().__init__()
        self.running = True
        # 准备工作
        self.th_id = 0
        if video_id == 'data/vd1.mp4':
            self.th_id = 1
        if video_id == 'data/vd2.mp4':
            self.th_id = 2
        self.dev = cv.VideoCapture(video_id)
        self.dev.open(video_id)


    def run(self):
        '''
        线程运行方法，读取视频帧并发出信号。
        :return: 无
        '''
        num = 0
        # 耗时操作
        while self.running:
            ret, frame = self.dev.read()
            frame, num = vehicle_detect(frame)
            if not ret:
                print('读取失败！')
            # car
            h, w, c = frame.shape
            # 将帧转换为字节
            img_bytes = frame.tobytes()
            self.send.emit(h, w, c, img_bytes, self.th_id, num, self.dev)

            QThread.usleep(1000000)

    def stop(self):
        self.running = False
        self.wait()
