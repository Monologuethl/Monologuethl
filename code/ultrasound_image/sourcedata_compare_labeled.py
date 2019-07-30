import cv2
import os
import shutil
root1 = r"C:\Users\2016\Desktop\compare\1"
root2 = r"C:\Users\2016\Desktop\compare\2"
root3 = r"C:\Users\2016\Desktop\compare\3"
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

# print(list1)
# print(list2)


list3 = []
for i in list1:
    for j in list2:
        if i == j:
            list3.append(i)
            image_path = os.path.join(os.path.join(root2), j+".jpg")
            # print(image_path)
            # shutil.move(image_path, root3)
print(len(list3))
print(list3)
count2 =0
index = []
for item in range(len(file_list1)):
    for j in list3:
        if (file_list1[item])[0:-4]==j:
            count2 = count2 +1
            index.append(item)
print(index)
print(len(index))
