import cv2
import os

root = r"D:\Tong\github\Unet-US\data\membrane\test"

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
