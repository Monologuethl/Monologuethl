import os
import numpy as np
from cv2 import cv2


def binary_photo(path):
    src = cv2.imread(path)  # 读取图像

    B = src[:, :, 0]
    G = src[:, :, 1]
    R = src[:, :, 2]

    src_new = B / 128 * 4 + G / 128 * 2 + R / 128
    cv2.imwrite(path, src_new)
    print(src_new.shape)
    print(path)


label1 = r"C:\Users\Tong\Desktop\label1"
label2 = r"C:\Users\Tong\Desktop\label2"
label3 = r"C:\Users\Tong\Desktop\label3"
label4 = r"C:\Users\Tong\Desktop\label4"

file_list = os.listdir(label3)  # 获取文件路径
count = 0
for item in file_list:
    photo_path = os.path.join(os.path.abspath(label3), item)
    # binary_photo(photo_path)
    results = cv2.imread(photo_path, 0)
    x, y = results.shape
    for i in range(x):
        for j in range(y):
            if results[i][j] ==3:
                results[i][j] =255
            else:
                results[i][j] =0
    count=count+1
    cv2.imwrite(photo_path, results)
    print(count)
