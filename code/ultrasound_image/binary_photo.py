import os
import numpy as np
from cv2 import cv2
import pylab


def binary_photo(path):
    src = cv2.imread(path)  # 读取图像

    B = src[:, :, 0]
    G = src[:, :, 1]
    R = src[:, :, 2]

    src_new = B/128*4 +G/128*2+R/128
    cv2.imwrite(path, src_new)
    print(path)


label = r"C:\Users\Tong\Desktop\label"
file_list = os.listdir(label)  # 获取文件路径

for item in file_list:
    photo_path = os.path.join(os.path.abspath(label), item)
    binary_photo(photo_path)
