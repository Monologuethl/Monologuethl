# ex2tron's blog:
# http://ex2tron.wang

import cv2
import os

path = r"C:\Users\Tong\Desktop\label"
edges_path = r"C:\Users\Tong\Desktop\edges"

path_list = os.listdir(path)


def track_back(x):
    pass


for i in path_list:
    img_path = os.path.join(path, i)

    img = cv2.imread(img_path, 0)
    # cv2.imshow('IMG', img)
    edges_img = os.path.join(edges_path, i)

    print(img_path)

    cv2.namedWindow('window')

    # 创建滑动条
    cv2.createTrackbar('maxVal', 'window', 100, 255, track_back)
    cv2.createTrackbar('minVal', 'window', 200, 255, track_back)

    while True:
        # 获取滑动条的值
        max_val = cv2.getTrackbarPos('maxVal', 'window')
        min_val = cv2.getTrackbarPos('minVal', 'window')

        edges = cv2.Canny(img, min_val, max_val)
        cv2.imshow('window', edges)
        # edges = edges[200:572, 0:606]
        cv2.imwrite(edges_img, edges)

        print(edges_img)
        # 按下ESC键退出
        if cv2.waitKey(30) == 27:
            break
