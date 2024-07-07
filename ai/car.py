import requests
import base64
import cv2 as cv


# opencv 图片
def vehicle_detect(img):
    '''
    使用百度API检测图像中的车辆。
    :param img:输入的OpenCV图像。
    :return:img:标识车辆信息的图像；num：车辆数目
    '''
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/vehicle_detect"
    '''
    imencode函数返回第一个值bool，第二个包含编码图像的字节缓冲区
    忽略第一个值，将img编码为JPEG格式
    '''
    _, encoded_image = cv.imencode('.jpg', img)
    # 转换为64位编码
    base64_image = base64.b64encode(encoded_image)
    params = {"image": base64_image}
    access_token = '24.59381b1222a5fc37c9fdcc17f1703bf5.2592000.1722493792.282335-89961110'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    num = 0
    print(response.json())
    if response:
        data = response.json()
        num = data['vehicle_num']['car']
        for item in data['vehicle_info']:
            location = item['location']
            '''
            绘制矩形标识车辆位置
            获取左上角坐标和右下角坐标，BGR（0，0，255）：红色，2：粗度为1
            '''
            # 左上角坐标
            x1 = location['left']
            y1 = location['top']
            # 右下角坐标
            x2 = x1 + location['width']
            y2 = y1 + location['height']
            # 绘制矩形，
            cv.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 1)
        # 定义要绘制的文字
            text = item['type']
            # 在画出的矩形框上面绘制文字
            position = (x1, y1-2)
            # 字体类型
            font = cv.FONT_HERSHEY_SIMPLEX
            # 字体大小
            font_scale = 1
            # BGR
            color = (0, 0, 255)  # 红色
            # 粗细
            thickness = 1
            # cv.LINE_AA：抗锯齿线条
            img = cv.putText(img, text, position, font, font_scale, color, thickness, cv.LINE_AA)
    return img, num
