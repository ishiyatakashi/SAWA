from SAWA.settings import BASE_DIR
import json


class path(object):
    def __init__(self):
        # カテゴリ（大分類）パス（固定値）
        self._pearentscategory_path = BASE_DIR + '/maindata/static/maindata/pearentsCategory/pearentsCategory.txt'
        # 各ディレクトリのパス（固定値）
        self.img_dir = BASE_DIR + '/maindata/static/maindata/Upload_image/'
        self.model_dir = BASE_DIR + '/maindata/static/maindata/model/'
        self.category_json_dir = BASE_DIR + '/maindata/static/maindata/category_json/'
        self.category_text_dir = BASE_DIR + '/maindata/static/maindata/category_text/'
        # 各ファイルのパス（変動）
        self._img_path = ''
        self._model_json_path = ''
        self._model_h5_path = ''
        self._category_json_path = ''
        self._category_text_path = ''

    @property
    def img_path(self):
        return self._img_path

    @img_path.setter
    def img_path(self, file_name):
        self._img_path = self.img_dir + file_name + '.jpg'

    @img_path.deleter
    def img_path(self):
        self._img_path = None

    @property
    def model_json_path(self):
        return self._model_json_path

    @model_json_path.setter
    def model_json_path(self, file_name: str):
        self._model_json_path = self.model_dir + file_name + '.json'

    @model_json_path.deleter
    def model_json_path(self):
        self._model_json_path = None

    @property
    def model_h5_path(self):
        return self._model_h5_path

    @model_h5_path.setter
    def model_h5_path(self, file_name: str):
        self._model_h5_path = self.model_dir + file_name + '.h5'

    @model_h5_path.deleter
    def model_h5_path(self):
        self._model_h5_path = None

    @property
    def category_json_path(self):
        return self._category_json_path

    @category_json_path.setter
    def category_json_path(self, file_name: str):
        self._category_json_path = self.category_json_dir + file_name + '.json'

    @category_json_path.deleter
    def category_json_path(self):
        self._category_json_path = None

    @property
    def category_text_path(self):
        return self._category_text_path

    @category_text_path.setter
    def category_text_path(self, file_name):
        self._category_text_path = self.category_text_dir + file_name + '.txt'

    @category_text_path.deleter
    def category_text_path(self):
        self._category_text_path = None

    @property
    def pearentscategory_path(self):
        return self._pearentscategory_path

    @pearentscategory_path.setter
    def pearentscategory_path(self, value):
        self._pearentscategory_path = value


class list(object):
    def __init__(self) -> object:
        self._category_dic = {}
        self._pearentscategorylist = []
        self._all_category = []

    @property
    def pearentscategorylist(self):
        pearents_path = path().pearentscategory_path
        with open(pearents_path, 'r+', encoding='utf-8') as f:
            self._pearentscategorylist = f.read().splitlines()
        return self._pearentscategorylist

    @pearentscategorylist.deleter
    def pearentscategorylist(self):
        self._pearentscategorylist = []

    @property
    def category_dic(self):
        return self._category_dic

    @category_dic.setter
    def category_dic(self, json_path):
        with open(json_path, 'r+', encoding='utf-8') as f:
            if __name__ == '__main__':
                self._category_dic = json.load(f)

    @category_dic.deleter
    def category_dic(self):
        self._category_dic = {}

    @property
    def all_category(self):
        return self._all_category

    @all_category.setter
    def all_category(self, text_path):
        with open(text_path, 'r+', encoding='utf-8') as f:
            self._all_category = f.read().splitlines()

    @all_category.deleter
    def all_category(self):
        self._all_category = []
