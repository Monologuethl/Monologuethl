import json
import os

path = r"D:\TONG\github\Monologuethl\dataset\json"
json_path = os.listdir(path)
print(len(json_path))
m = 0
for i in json_path:
    src = os.path.join(os.path.abspath(path), i)
    with open(src, 'r') as f:
        data = json.load(f)

        # print(type(data))
        # print(data["shapes"][0])
        # print(type(data["shapes"][0]))
        # print(len(data["shapes"]))

        dict1 = data["shapes"][0]
        dict2 = data["shapes"][1]
        dict3 = data["shapes"][2]
        dict4 = data["shapes"][3]

        s = str(m)

        json_1 = os.path.join(os.path.abspath(path), s + "_1.json")
        json_2 = os.path.join(os.path.abspath(path), s + "_2.json")
        json_3 = os.path.join(os.path.abspath(path), s + "_3.json")
        json_4 = os.path.join(os.path.abspath(path), s + "_4.json")

        list_dict1 = [dict1]
        data["shapes"] = list_dict1

        with open(json_1, 'w') as f:
            json.dump(data, f)

        list_dict2 = [dict2]
        data["shapes"] = list_dict2

        with open(json_2, 'w') as f:
            json.dump(data, f)

        list_dict3 = [dict3]
        data["shapes"] = list_dict3

        with open(json_3, 'w') as f:
            json.dump(data, f)

        list_dict4 = [dict4]
        data["shapes"] = list_dict4

        with open(json_4, 'w') as f:
            json.dump(data, f)

        m = m + 1
