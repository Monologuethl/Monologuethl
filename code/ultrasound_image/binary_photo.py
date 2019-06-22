import os
import numpy as np
from cv2 import cv2
import pylab

def binary_photo(path):
    src = cv2.imread(path)  # 读取图像

    R = src[:, :, 2]

    # x, y = R.shape
    # for i in range(x):
    #     for j in range(y):
    #         print(i, j)
    #         if R[i, j] != 255:
    #             R[i, j] = 0

    src_new = np.zeros(src.shape).astype("uint8")
    src_new[:, :, 0] = R
    src_new[:, :, 1] = R
    src_new[:, :, 2] = R
    cv2.imwrite(path, src_new)
    print(path)


label = r"D:\TONG\github\Monologuethl\code\photo_tools"
file_list = os.listdir(label)  # 获取文件路径

for item in file_list:
    photo_path = os.path.join(os.path.abspath(label), item)
    binary_photo(photo_path)