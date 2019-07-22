import cv2
import matplotlib.pyplot as plt
path1 = r"C:\Users\Tong\Desktop\label\6.png"
path2 = r"C:\Users\Tong\Desktop\us_label\6.png"
img1 = cv2.imread(path1)
img2 = cv2.imread(path2)
# cv2.imshow("img", img)
# cv2.waitKey(0)


plt.imshow(img2)
plt.show()



