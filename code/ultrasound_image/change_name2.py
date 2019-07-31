import cv2
import os

root = r"C:\Users\2016\Desktop\corp_512\image"

file_list = os.listdir(root)  # 获取文件路径
print(file_list)
for item in file_list:
    photo_path = os.path.join(os.path.abspath(root), item)
    print(item[0:-4])
    img = cv2.imread(photo_path)
    print(img.shape)
    path =os.path.join(os.path.abspath(root), item[0:-4]+".png")
    print(path)
    cv2.imwrite(path, img)
