import os
import cv2

path1 = r"C:\Users\Tong\Desktop\Fat4"
path2 = r"C:\Users\Tong\Desktop\Peritoneal4"
path3 = r"C:\Users\Tong\Desktop\Skin4"
path4 = r"C:\Users\Tong\Desktop\Subcutaneous4"

filelist = os.listdir(path1)  # 获取文件路径


total_num = len(filelist)  # 获取文件长度（个数）
i = 0  # 表示文件的命名是从1开始的
print(filelist)
for item in filelist:
    src = os.path.join(os.path.abspath(path4), item)
    image = cv2.imread(src)
    cropImg1 = image[256:512, 256:512]
    # cropImg_0 = image[0:256, 0:256]
    # cropImg_1 = image[256:512, 0:256]
    # cropImg_2 = image[0:256, 256:512]
    # cropImg_3 = image[256:512, 256:512]

    # cv2.imwrite(r"C:\Users\Tong\Desktop\new_Subcutaneous\\"+str(i)+"_0.jpg", cropImg_0)
    #
    # cv2.imwrite(r"C:\Users\Tong\Desktop\new_Subcutaneous\\"+str(i)+"_1.jpg", cropImg_1)
    #
    # cv2.imwrite(r"C:\Users\Tong\Desktop\new_Subcutaneous\\"+str(i)+"_2.jpg", cropImg_2)
    #
    # cv2.imwrite(r"C:\Users\Tong\Desktop\new_Subcutaneous\\"+str(i)+"_3.jpg", cropImg_3)

    cv2.imwrite(src, cropImg_3)
    # cv2.imwrite(src, cropImg2)

