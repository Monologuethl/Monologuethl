import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

path = r"C:\Users\Tong\Desktop\Unet-US\data\membrane\train\image"

for i in os.listdir(path):
    label_path = os.path.join(os.path.abspath(path), i)
    print(label_path)
    img = cv2.imread(label_path)
    B = img[:, :, 0]
    G = img[:, :, 1]
    R = img[:, :, 2]
    x, y = R.shape
    src_new = np.zeros(R.shape).astype("uint8")
    for m in range(x):
        for n in range(y):
            src_new[m, n] = 0.30 * B[m, n] + 0.59 * G[m, n] + 0.11 * R[m, n]
    cv2.imwrite(label_path, src_new)
