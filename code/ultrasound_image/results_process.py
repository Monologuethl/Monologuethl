import cv2
import matplotlib.pyplot as plt
import os

path = r"D:\Tong\github\Unet-US\data\membrane\result"
file_list = os.listdir(path)  # 获取文件路径

for item in file_list:
    photo_path = os.path.join(os.path.abspath(path), item)

    img = cv2.imread(photo_path, 0)
    img[img > 127] = 255
    img[img < 127] = 0
    # plt.imshow(img)
    # plt.show()
    #
    # plt.hist(img.ravel(), 256, [0, 256])
    # plt.show()
    cv2.imwrite(photo_path, img)
