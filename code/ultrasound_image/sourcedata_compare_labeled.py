import cv2
import os

root1 = r"C:\Users\2016\Desktop\compare\1"
root2 = r"C:\Users\2016\Desktop\compare\2"
list1 = []
list2 = []
file_list1 = os.listdir(root1)  # 获取文件路径
# print(file_list1)
for item in file_list1:
    photo_path = os.path.join(os.path.abspath(root1), item)
    list1.append(item[0:-4])
    # print(photo_path)

file_list2 = os.listdir(root2)  # 获取文件路径
# print(file_list2)
for item in file_list2:
    photo_path = os.path.join(os.path.abspath(root2), item)
    list2.append(item[0:-4])
    # print(photo_path)

print(list1)
print(list2)
count = 0
for i in list1:
    for j in list2:
        if i == j:
            print(i)
            count = count + 1
print(count)
