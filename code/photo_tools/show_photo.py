import cv2
import matplotlib.pyplot as plt
img = cv2.imread(r"D:\TONG\github\Monologuethl\us_label\2.jpg")
R = img[:, :, 2]
# cv2.imshow("img", img)
# cv2.waitKey(0)

plt.imshow(img)
plt.show()

plt.hist(R.ravel(), 256, [0, 256])
plt.show()
