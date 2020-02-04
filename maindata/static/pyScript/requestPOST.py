import cgi
import sys
import io
import base64
from typing import List, Any
from keras.models import load_model
from keras.preprocessing.image import img_to_array, load_img
import os

from PIL import Image
import sys

from django.core.files.storage import FileSystemStorage
from SAWA.settings import BASE_DIR
import random
from io import BytesIO
import maindata.static.property.category as pr


class requestPOST(object):
    def __init__(self):
        self.pr_path = pr.path()
        self.pr_list = pr.list()
        del self.pr_path.img_path
        del self.pr_path.category_text_path
        del self.pr_path.category_json_path
        del self.pr_path.model_h5_path
        del self.pr_path.model_json_path

    def image_file_create(self):
        binary_image = request.POST.get('base64')
        # 保存用のメソッド
        fileobject = FileSystemStorage()
        # ファイルの名前を作成
        filename = 'request_image' + str(random.randint(1, 1000000000)) + '.jpg'
        # ファイルをバイナリから作る
        binary = base64.b64decode(binary_image.splt(',')[1])
        img = Image.open(BytesIO(binary))
        # 保存場所の
        self.pr_path.img_path(filename)
        # 保存する
        img.save(self.pr_path.img_path)

    def study(self, request):
        image_file_create()
        pearList = self.pr_list.pearentsCategoryList
        select_dic = {}
        result_dic = []
        category_table = {}
        category_all = {}
        return_dic = {}
        for i in pearList:
            select_list = request.POST.get(i)
            if select_list is not None:
                select_dic[i] = select_list
                category_table[i] = self.pr_list.category_dic(i)
                category_all[i] = self.pr_list.all_category(i)
        for i in select_dic.keys():
            pred_list = []
            model_path = self.pr_path.model_h5_path(i)
            # 学習済みモデルの読込
            model = load_model(model_path)
            # 画像の読込
            img = img_to_array(load_img(img_path, target_size=(224, 224)))
            # 0-1に変換
            img_nad = img_to_array(img) / 255
            # 4次元配列に
            img_nad = img_nad[None, ...]
            # 判定結果をリストに
            pred_data = model.predict(self.img_nad, batch_size=1, verbose=0)
            for pred in pred_data:
                for score in pred:
                    pred_list.append(score)
            # 判定結果とカテゴリリストで辞書型を生成
            dic = {key: val for key, val in zip(category_all[i], pred_list)}
            result_dic[i] = dic

        for pCategory, categpryList in select_dic.items():
            for selectCategory in categpryList:
                for id, value in result_dic[pCategory].items():
                    if selectCategory == id:
                        return_dic[selectCategory] = value
                for roma, japan in category_table[pCategory]:
                    for key in retrun_dic.keys():
                        if key == roma:
                            return_dic[japan] = retrun_dic.pop(key)
        for k, v in sorted(return_dic.items(), key=lambda x: x[-1]):
            sort_return_dic[k] = v

        return sort_return_dic
