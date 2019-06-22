import os

for i in range(104):
    cmd_commend1 = r"labelme_json_to_dataset  {}.json".format(i)
    os.system(cmd_commend1)
