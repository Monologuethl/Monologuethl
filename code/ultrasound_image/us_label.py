import os
import numpy as np
from cv2 import cv2


def binary_photo(path):
    src = cv2.imread(path)  # 读取图像

    B = src[:, :, 0]
    G = src[:, :, 1]
    R = src[:, :, 2]

    src_new = np.zeros(R.shape).astype("uint8")
    src_new = 0.30 * B+ 0.59 * G + 0.11 * R
    cv2.imwrite(path, src_new)
    print(path)


label = r"C:\Users\Tong\Desktop\us\corp\images"
file_list = os.listdir(label)  # 获取文件路径

for item in file_list:
    photo_path = os.path.join(os.path.abspath(label), item)
    binary_photo(photo_path)
