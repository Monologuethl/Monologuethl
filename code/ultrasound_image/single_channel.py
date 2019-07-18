import os
import numpy as np
from cv2 import cv2
import pylab

def single_channel(path):
    src = cv2.imread(path)  # 读取图像

    R = src[:, :, 2]
    src_new = R
    cv2.imwrite(path, src_new)
    print(path)


label = r"C:\Users\Tong\Desktop\U-Net\new_label_256"
file_list = os.listdir(label)  # 获取文件路径

for item in file_list:
    photo_path = os.path.join(os.path.abspath(label), item)
    single_channel(photo_path)