import os
import shutil

json_path = r"D:\TONG\github\Monologuethl\dataset\label_path"
line_path = r"D:\TONG\github\Monologuethl\dataset\line_label"

json_list = os.listdir(json_path)

print(json_list)

for i in json_list:

    label_dir = os.path.join(json_path, i)

    for j in os.listdir(label_dir):
        if j == 'label.png':
            label_img_dir = os.path.join(label_dir, j)

    num_label_path = os.path.join(line_path, i[0:-5]+'.png')

    shutil.copy(label_img_dir, num_label_path)


