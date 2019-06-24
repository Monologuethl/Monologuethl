import os

for i in range(104):
    for j in range(1, 5):
        cmd_commend1 = r"labelme_json_to_dataset  {}_{}.json".format(i, j)
        os.system(cmd_commend1)
