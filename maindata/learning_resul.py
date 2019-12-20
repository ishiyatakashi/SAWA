#!/usr/bin/env python
# coding: utf-8

# In[2]:

import cgi
import os
import self_package
from self_package import image_operation


def __init__(self):
    # LISTの初期化
    self.result_dic = {}
    self.category_key_list = []
    self.category_japanese_list = []
    self.sort_result_dic = []

    # ファイルの参照パス指定

    self.img_dir = os.path.abspath('maindata/static/maindata/uplode_img')
    self.img_path = image_operation.addpath(self.img_dir)


def select_learning(self):
    json_path = os.path.abspath('./static/maindata/json/category.json')
    #  フィールドストレージからpostを取得しリストに格納
    form = cgi.FildStorage()
    select_list = form.getlist('selectCategory')

    #  カテゴリーテーブルの作成,選択されたカテゴリーIDをカテゴリーKEYに変換したリストの作成
    select_list = self_package.category.name_change(select_list, json_path)
    category_table = self_package.category.creat_category_table(json_path)
    for category in category_table.items():
        self.category_key_list.append(category.keys())

    #  リクエストされた画像を学習し、結果を辞書型で作成
    dic = self_package.study.learning(self.img_path, self.category_key_list)

    #  選択したカテゴリーの結果を整理する
    for select in select_list:
        for resultValue in dic.items():
            if select == resultValue.keys():
                self.result_dic[select] = resultValue.values()
                for japanese in category_table.items():
                    if japanese.keys() == select:
                        self.result_dic[select] = self.result_dic[japanese.values()['japanese']]
    revers_result = sorted(self.result_dic.items(), key=lambda x: x[0], reverse=True)
    first_key, first_value = revers_result[0]
    second_key, second_value = revers_result[1]
    for k,v in revers_result:
        self.sort_result_dic[k] = v

    return self.sort_result_dic, first_key, second_key



