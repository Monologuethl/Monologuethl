import os
import shutil

# path = r"C:\Users\Tong\Desktop\test_data\json\0_1_json"
# count = 0
# for file in os.listdir(path):
#     if file.endswith("label.png"):
#         os.rename(os.path.join(path, file), os.path.join(path, str(count) + ".png"))
#         count += 1

corp_img = r"D:\TONG\github\Monologuethl\code\ultrasound_image\corp_img"
img_path = r"D:\TONG\github\Monologuethl\code\ultrasound_image\img"
label_path = r"D:\TONG\github\Monologuethl\code\ultrasound_image\label"

filelist = os.listdir(corp_img)

print(filelist)
for i in filelist:
    label_name = i[0:-5]
    # print(label_name)
    json_path = os.path.join(os.path.abspath(corp_img), i)
    # print(label_path)
    img = os.path.join(os.path.abspath(json_path), 'img.png')
    label = os.path.join(os.path.abspath(json_path), 'label.png')

    shutil.move(img, img_path)
    shutil.move(label, label_path)
    new_img = os.path.join(os.path.abspath(img_path), 'img.png')
    new_label = os.path.join(os.path.abspath(label_path), 'label.png')

    os.rename(new_img, os.path.join(os.path.abspath(img_path), label_name + '.png'))
    os.rename(new_label, os.path.join(os.path.abspath(label_path), label_name + '.png'))
