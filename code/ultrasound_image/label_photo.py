import os
import pylab

import matplotlib.pyplot as plt
import numpy as np
from cv2 import cv2


def process_RGB_channel(path_0, path_1):
    src = cv2.imread(path_0)
    B = src[:, :, 0]
    G = src[:, :, 1]
    R = src[:, :, 2]
    x, y = R.shape
    for i in range(x):
        for j in range(y):
            print(i, j)
            if R[i, j] < 170:
                R[i, j] = 0
                G[i, j] = 0
                B[i, j] = 0
            if G[i, j] > 160:
                R[i, j] = 0
                G[i, j] = 0
                B[i, j] = 0
            if B[i, j] > 160:
                R[i, j] = 0
                G[i, j] = 0
                B[i, j] = 0

    src_new = np.zeros(src.shape).astype("uint8")
    src_new[:, :, 0] = B
    src_new[:, :, 1] = G
    src_new[:, :, 2] = R
    cv2.imwrite(path_1, src_new)


def process_closing(path_1, path_2):
    img = cv2.imread(path_1, 2)
    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (30, 30))
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    cv2.imwrite(path_2, closing)


def binary_photo(path):
    src = cv2.imread(path)
    R = src[:, :, 2]
    x, y = R.shape
    for i in range(x):
        for j in range(y):
            print(i, j)
            if R[i, j] < 30:
                R[i, j] = 0
            else:
                R[i, j] = 255
            print(R[i, j])

    src_new = np.zeros(src.shape).astype("uint8")
    src_new[:, :, 0] = R
    src_new[:, :, 1] = R
    src_new[:, :, 2] = R
    cv2.imwrite(path, src_new)
    print(path)


def show_photo(path):
    img = cv2.imread(path)
    R = img[:, :, 2]
    # cv2.imshow("img", img)
    # cv2.waitKey(0)
    plt.imshow(img)
    plt.show()
    # plt.hist(R.ravel(), 256, [0, 256])
    # plt.show()


path_0 = r"D:\TONG\github\Monologuethl\corp_img\0.jpg"
path_1 = r"D:\TONG\github\Monologuethl\us_label\1.jpg"
path_2 = r"D:\TONG\github\Monologuethl\us_label\2.jpg"


if __name__ == '__main__':

    # process_RGB_channel(path_0, path_1)
    process_closing(path_1, path_2)
    binary_photo(path_2)
    show_photo(path_2)

# -----------------------------------------------------

#
# plt.hist(B.ravel(), 256, [0, 256])
# plt.show()
#
# pylab.imshow(B)
# pylab.show()
#
# plt.hist(G.ravel(), 256, [0, 256])
# plt.show()
#
# pylab.imshow(G)
# pylab.show()
#
# plt.hist(R.ravel(), 256, [0, 256])
# plt.show()
#
# pylab.imshow(R)
# pylab.show()

# a1 = np.array([1,2,3,4],dtype=np.complex128)
# print(a1)
# print("数据类型",type(a1))           #打印数组数据类型
# print("数组元素数据类型：",a1.dtype) #打印数组元素数据类型
# print("数组元素总数：",a1.size)      #打印数组尺寸，即数组元素总数
# print("数组形状：",a1.shape)         #打印数组形状
# print("数组的维度数目",a1.ndim)      #打印数组的维度数目
