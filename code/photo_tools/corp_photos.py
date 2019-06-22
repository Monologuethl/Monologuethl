import os
import cv2

filelist = os.listdir(r"D:\TONG\github\Monologuethl\us_image")  # 获取文件路径
total_num = len(filelist)  # 获取文件长度（个数）
i = 0  # 表示文件的命名是从1开始的
print(filelist)
for item in filelist:
    src = os.path.join(os.path.abspath(r"D:\TONG\github\Monologuethl\us_image"), item)
    image = cv2.imread(src)
    cropImg = image[125:731, 235:857]
    cv2.imwrite(r"D:\TONG\github\Monologuethl\corp_img\\"+str(i)+".jpg", cropImg)
    i = i + 1
