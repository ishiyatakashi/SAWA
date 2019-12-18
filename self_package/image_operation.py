#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import glob
import os
import subprocess

path_list = []
ct = 0


def reset(path):
    # imgフォルダ内のファイルパスリストと参照引数をリセットする。
    global ct
    global path_list
    path = path + '/'
    if ct > 40:
        subprocess.call(["del", "/q", path])
        path_list = []
        ct = 0


def add_path(path):
    global path_list
    global ct
    new_path_list = glob.glob(os.path.join(path, '*.jpg'))
    if path_list != new_path_list:
        path_list = new_path_list
    path = path_list[ct]
    ct = ct + 1
    return path
