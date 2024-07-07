from PyQt5.QtCore import QThread
import cv2 as cv
from PyQt5.QtCore import pyqtSignal
from ai.human import People_detect

class VideoPeople(QThread):
    # 自定义信号类型，用于传递视频帧数据
    send = pyqtSignal(int, int, int, bytes, int, int, object) #emit
    def __init__(self,video_id):
        '''
        初始化视频线程。
        :param video_id:视频文件路径。
        '''
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
        :return:无
        '''
        num = 0
        # 耗时操作
        while self.running:
            ret, frame = self.dev.read()
            frame, num = People_detect(frame)
            if not ret:
                print('no')
            # car
            h, w, c = frame.shape
            img_bytes = frame.tobytes()
            self.send.emit(h, w, c, img_bytes, self.th_id, num, self.dev)

            QThread.usleep(1000000)

    def stop(self):
        self.running = False
        self.wait()




