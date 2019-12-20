#!/usr/bin/env python
# coding: utf-8

# In[2]:
from typing import Union

import self_package
import cgi
import os

from self_package import image_operation

# LISTの初期化
result_dic = {}
category_key_list = []
category_japanese_list = []

# ファイルの参照パス指定
json_path = os.path.abspath('./static/maindata/json/category.json')
img_dir = os.path.abspath('maindata/static/maindata/uplode_img')
img_path = image_operation.addpath(img_dir)

#  フィールドストレージからpostを取得しリストに格納
form = cgi.FildStorage()
select_list = form.getlist('selectCategory')

#  カテゴリーテーブルの作成,選択されたカテゴリーIDをカテゴリーKEYに変換したリストの作成
select_list = self_package.category.name_change(select_list, json_path)
category_table = self_package.category.creat_category_table(json_path)
for category in category_table.items():
    category_key_list.append(category.keys())

#  リクエストされた画像を学習し、結果を辞書型で作成
dic = self_package.study.learning(img_path, category_key_list)

#  選択したカテゴリーの結果を整理する
for select in select_list:
    for resultValue in dic.items():
        if select == resultValue.keys():
            result_dic[select] = resultValue.values()
            for japanese in category_table.items():
                if japanese.keys() == select:
                    result_dic[select] = result_dic[japanese.values()['japanese']]
revers_result = sorted(result_dic.items(), key=lambda x: x[0], reverse=True)
first_key, first_value = revers_result[0]
second_key, second_value = revers_result[1]

print("""
{% extends "maindata/bace.html" %}

{% block title %}{% endblock title %}

{% block content %}

    <div id="wrapper">
        <div class="center" style="font-size: 40px">あなたは....</div>
        <div class="center" style="font-size: 50px"><a style="font-size: 60px">{first}</a>っぽい
            <a style="font-size: 60px">{second}</a>です</div>
        <div><a style='font-size: 35px' </div>
        <div class="details">
        
        """.format(first=first_key, second=second_key))
for result in revers_result:
    key, value = result
    print("""
            <div class='box'>
            <a style='font-size: 30px'>{key}</a>
            <a style='font-size: 30px'>{value}</a>
            </div>   
    """.format(key=key,value=value))
print("""
        </div>
     </div

    <!-- Twitter 共有ボタンスクリプト -->
    <a href="https://twitter.com/share?ref_src=twsrc%5Etfw" class="twitter-share-button" data-size="large"
       data-text="あなたは〇〇っぽい？" data-lang="ja" data-show-count="false">Tweet</a>
    <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

    <!-- Facebook 共有ボタンスクリプト (保留!!!!)-->
    <!--
    <div id="fb-root"></div>
    <script async defer crossorigin="anonymous" src="https://connect.facebook.net/ja_JP/sdk.js#xfbml=1&version=v5.0"></script>
    <div class="fb-share-button" data-href="https://developers.facebook.com/docs/plugins/" data-layout="button" data-size="small"><a target="_blank" href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Fplugins%2F&amp;src=sdkpreparse" class="fb-xfbml-parse-ignore" style="font-size: 10px">シェア</a></div>
    -->
{% endblock content %}""".format())
self_package.image_operation.reset(img_dir)
