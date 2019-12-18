#!/usr/bin/env python
# coding: utf-8

# In[2]:
from typing import Union

import

import self_package
import cgi
import os

from self_package import image_operation

result_dic = {}
json_path = os.path.abspath("./static/maindata/json/category.json")
img_dir = os.path.abspath('./static/maindata/uplode_img')
form = cgi.FildStorage()
select_list = form.getlist('selectCategory')
select_list = self_package.category.name_change(select_list, json_path)
category_table = self_package.category.creat_category_table(json_path)
img_path = image_operation.addpath(img_dir)
dic = self_package.study.learning(img_path, category_table)

for select in select_list:
    for resultValue in dic.items():
        if select == resultValue.keys():
            result_dic[select] = resultValue.values()

self_package.image_operation.reset(img_dir)
            



