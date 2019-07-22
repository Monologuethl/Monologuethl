import cv2
import matplotlib.pyplot as plt
photo_path = r"C:\Users\Tong\Desktop\0.png"
crop_size = (256, 256)
img = cv2.imread(photo_path)
img_new = cv2.resize(img, crop_size, interpolation=cv2.INTER_NEAREST)

plt.imshow(img_new)
plt.show()

plt.hist(img_new.ravel(), 256, [0, 256])
plt.show()
