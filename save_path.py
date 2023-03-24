# !/usr/bin/env python
# -*- encoding: utf-8 -*-

import os

img_path = 'datasets/mydata721/images/train/' # 图片的绝对路径，注意最后加上 /
save_txt = 'mydata82/train.txt' # 保存在txt文件中。
img_list = os.listdir(img_path)
print('img_list: ', img_list)

with open(save_txt, 'w') as f:
    for img_name in img_list:
        f.write(img_path+img_name + '\n')
