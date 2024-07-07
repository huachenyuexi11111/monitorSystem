import cv2 as cv
# encoding:utf-8

import requests
import base64
import numpy as np
import json

'''
人流量统计
'''

def People_detect(img):
    '''
    使用百度API检测图像中的人数。
    :param img:输入的OpenCV图像。
    :return:img:渲染后的图片；num：当前人数
    '''
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_num"
    # 二进制方式打开图片文件
    _, encoded_image = cv.imencode('.jpg', img)
    base64_image = base64.b64encode(encoded_image).decode('utf-8')

    # 将参数show设置为true，使返回渲染后的图片
    params = {"image": base64_image, "show": "true"}

    access_token = '24.9c15c73ac0335bd1eb4aa3c61f60d49c.2592000.1722752710.282335-90934458'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded',
                               'Accept':'application/json'
               }
    response = requests.post(request_url, data=params, headers=headers)
    print(response.json())
    if response:
        data = response.json()
        # 接收渲染后的图片
        img = data['image']
        # 将接收到的64位编码的图像解码
        img = base64.b64decode(img)
        # 将解码后的二进制数据转换为一个 numpy 数组
        img = np.frombuffer(img, np.uint8)
        # 将 numpy 数组形式的图像数据解码为 OpenCV 图像格式
        img = cv.imdecode(img, cv.IMREAD_COLOR)
        num = data['person_num']
        return img, num