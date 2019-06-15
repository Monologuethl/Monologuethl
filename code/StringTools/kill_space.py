# encoding = utf-8#
import os

with open((os.path.join('1.txt')), 'r') as f:
    data = f.readlines()
    for line in data:
        odom = line.split()
        tmp_str = "".join(odom)
        result = ' '.join(tmp_str.split())

with open((os.path.join('test_copy.txt')), 'w') as f:
    f.write(result)
