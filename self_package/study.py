#!/usr/bin/env python
# coding: utf-8

# In[1]:


from keras.models import load_model
from keras.preprocessing.image import img_to_array, load_img


def learning(self, model_path, img_path, category_key):
    pred_list = []
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
    dic = {key: val for key, val in zip(category_key, pred_list)}
    return dic

# In[ ]:
