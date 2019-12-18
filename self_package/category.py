#!/usr/bin/env python
# coding: utf-8


import json
from typing import List, Any


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
       category_table:list型のカテゴリーテーブル
    """

    category_table: List[Any] = []
    with open(path, 'r', encoding='UTF-8')as f:
        categories_dic = json.load(f)
    for categories in self.categories_list:
        category_table.append(categories.keys())
    return category_table
