import os
import shutil

Skin = r"C:\Users\Tong\Desktop\label\Skin"
Fat = r"C:\Users\Tong\Desktop\label\Fat"
Subcutaneous = r"C:\Users\Tong\Desktop\label\Subcutaneous"
Peritoneal = r"C:\Users\Tong\Desktop\label\Peritoneal"

Path = r"C:\Users\Tong\Desktop\label\Skin"
filelist = os.listdir(Path)
print(filelist)
print(len(filelist))

# for i in filelist:
#     label_photo = os.path.join(os.path.abspath(Path), i)
#     print(label_photo)
#     if i[-5] == '2':
#         shutil.move(label_photo, Fat)
#     if i[-5] =='3':
#         shutil.move(label_photo, Subcutaneous)
#     if i[-5] =='4':
#         shutil.move(label_photo, Peritoneal)

