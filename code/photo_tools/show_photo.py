import cv2
import matplotlib.pyplot as plt

path1 = r"C:\Users\2016\Desktop\compare\label\3.png"
img1 = cv2.imread(path1)
# cv2.imshow("img", img)
# cv2.waitKey(0)
# R = img1[:, :, 2]
plt.imshow(img1)
plt.show()

plt.hist(img1.ravel(), 256, [0, 256])
plt.show()

# plt.imshow(img2)
# plt.show()

# plt.hist(img2.ravel(), 256, [0, 256])
# plt.show()

# 124.5 855.5
# 235.5 731.5
