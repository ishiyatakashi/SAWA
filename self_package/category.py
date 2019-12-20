#!/usr/bin/env python
# coding: utf-8


import json
from typing import List, Any

category_dic = {}


def name_change(path, change_list) -> object:
    """getパラメータをカテゴリー名に変換する:
        @param
         path :jsonファイルを参照するための絶対パス
         change_list:getパラメータから抽出した選択したカテゴリーのリスト
        @return
         select_categories :list[] 選択したカテゴリー名の変換後リスト
        @except
        FileExistsError:スルー
    """

    select_categories: List[Any] = []
    try:
        with open(path, 'r', encoding='UTF-8')as f:
            category_table = json.load(f)
        for param in change_list:
            for tag in category_table:
                if tag["id"] == param:
                    select_categories.append(tag.keys())
        return select_categories
    except FileExistsError:
        return FileExistsError


def creat_category_table(self, path):
    """カテゴリーテーブルの作成
    　@param
       path:jsonフォルダの絶対パス

      @return
       category_table:dic型のカテゴリーテーブル
    """

    global category_dic
    with open(path, 'r', encoding='UTF-8')as f:
        new_categories_dic = json.load(f)
    if category_dic is None or category_dic != new_categories_dic:
        category_dic = new_categories_dic

    return category_dic
