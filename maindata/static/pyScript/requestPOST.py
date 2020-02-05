import base64
import random
from io import BytesIO

from PIL import Image
from keras.models import load_model
from keras.preprocessing.image import img_to_array, load_img

import maindata.static.property.category as pr


class requestPOST(object):
    def __init__(self):
        self.pr_path = pr.path()
        self.pr_list = pr.list()

    def image_file_create(self, request):
        binary_image = request.POST.get('base64')
        print(binary_image)
        # ファイルの名前を作成
        filename = 'request_image' + str(random.randint(1, 10)) + '.jpg'
        # ファイルをバイナリから作る
        binary = base64.b64decode(binary_image.split(',')[1])
        img = Image.open(BytesIO(binary))
        # 保存場所の
        self.pr_path.img_path = filename
        # 保存する
        img.save(self.pr_path.img_path)

    def study(self, request):
        requestPOST.image_file_create(self, request)
        image_path = self.pr_path.img_path
        pearList = self.pr_list.pearentscategorylist
        select_dic = {}
        result_dic = []
        category_table = {}
        category_all = {}
        return_dic = {}
        sort_return_dic = {}
        for i in pearList:
            select_list = request.POST.get(i)
            if select_list is not None:
                self.pr_path.category_json_path = i
                self.pr_path.category_text_path = i
                select_dic[i] = select_list
                self.pr_list.all_category = self.pr_path.category_text_path
                self.pr_list.category_dic = self.pr_path.category_json_path
                category_table[i] = self.pr_list.category_dic
                category_all[i] = self.pr_list.all_category
        for i in select_dic.keys():
            pred_list = []
            self.pr_path.model_h5_path = i
            model_path = self.pr_path.model_h5_path
            # 学習済みモデルの読込
            model = load_model(model_path, compile=False)
            # 画像の読込
            img = img_to_array(load_img(image_path, target_size=(224, 224)))
            # 0-1に変換
            img_nad = img_to_array(img) / 255
            # 4次元配列に
            img_nad = img_nad[None, ...]
            # 判定結果をリストに
            pred_data = model.predict(img_nad, batch_size=1, verbose=0)
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
                    for key in return_dic.keys():
                        if key == roma:
                            return_dic[japan] = return_dic.pop(key)
        for k, v in sorted(return_dic.items(), key=lambda x: x[-1]):
            sort_return_dic[k] = v

        return sort_return_dic
