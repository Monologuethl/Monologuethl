import cv2
import matplotlib.pyplot as plt
path1 = r"D:\Tong\github\Unet-US\data\membrane\test\0_predict.png"
img1 = cv2.imread(path1)
# cv2.imshow("img", img)
# cv2.waitKey(0)
R = img1[:, :, 2]
plt.imshow(img1)
plt.show()


plt.hist(img1.ravel(), 256, [0, 256])
plt.show()

# plt.imshow(img2)
# plt.show()

# plt.hist(img2.ravel(), 256, [0, 256])
# plt.show()

