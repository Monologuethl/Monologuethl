import os
import numpy as np
from cv2 import cv2
import pylab


def single_channel(path):
    src = cv2.imread(path)  # 读取图像
    R = src[:, :, 2]
    src_new = R
    cv2.imwrite(path, src_new)
    print(src_new.shape)
    print(path)


root = r"C:\Users\Tong\Desktop\us\corp\images"
path1 = r"C:\Users\Tong\Desktop\us\corp\Fat"
path2 = r"C:\Users\Tong\Desktop\us\corp\Peritoneal"
path3 = r"C:\Users\Tong\Desktop\us\corp\Skin"
path4 = r"C:\Users\Tong\Desktop\us\corp\Subcutaneous"
label = r"C:\Users\Tong\Desktop\label"

label1 = r"C:\Users\Tong\Desktop\label1"
label2 = r"C:\Users\Tong\Desktop\label2"
label3 = r"C:\Users\Tong\Desktop\label3"
label4 = r"C:\Users\Tong\Desktop\label4"

file_list = os.listdir(label)  # 获取文件路径

for item in file_list:
    photo_path = os.path.join(os.path.abspath(label), item)
    single_channel(photo_path)
