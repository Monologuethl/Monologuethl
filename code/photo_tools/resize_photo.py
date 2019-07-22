import cv2
import os

root = r"C:\Users\Tong\Desktop\img"
label = r"C:\Users\Tong\Desktop\label"


label1 = r"C:\Users\Tong\Desktop\label1"
label2 = r"C:\Users\Tong\Desktop\label2"
label3 = r"C:\Users\Tong\Desktop\label3"
label4 = r"C:\Users\Tong\Desktop\label4"

def single_channel(path):
    src = cv2.imread(path)  # 读取图像
    R = src[:, :, 2]
    src_new = R
    cv2.imwrite(path, src_new)
    print(src_new.shape)
    print(path)


file_list = os.listdir(root)  # 获取文件路径
print(file_list)
for item in file_list:
    photo_path = os.path.join(os.path.abspath(root), item)
    crop_size = (256, 256)
    img = cv2.imread(photo_path)
    img_new = cv2.resize(img, crop_size, interpolation=cv2.INTER_NEAREST)

    cv2.imwrite(photo_path, img_new)

    # 单通道
    single_channel(photo_path)

    # CV_INTER_NN - 最近邻插值,  
    # CV_INTER_LINEAR - 双线性插值 (缺省使用)  
    # CV_INTER_AREA - 使用象素关系重采样。当图像缩小时候，该方法可以避免波纹出现。当图像放大时，类似于 CV_INTER_NN 方法..  
    # CV_INTER_CUBIC - 立方插值. 
