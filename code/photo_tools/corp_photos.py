import os
import cv2

filelist = os.listdir(r"C:\Users\Tong\Desktop\U-Net\train_labels")  # 获取文件路径
total_num = len(filelist)  # 获取文件长度（个数）
i = 0  # 表示文件的命名是从1开始的
print(filelist)
for item in filelist:
    src = os.path.join(os.path.abspath(r"C:\Users\Tong\Desktop\U-Net\train_labels"), item)
    image = cv2.imread(src)
    cropImg = image[0:512, 0:512]
    cv2.imwrite(r"C:\Users\Tong\Desktop\new_label\\"+str(i)+".jpg", cropImg)
    i = i + 1
