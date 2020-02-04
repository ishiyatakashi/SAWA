from SAWA.settings import BASE_DIR
import json


class path(object):
    def __init__(self):
        # カテゴリ（大分類）パス（固定値）
        self.pearentsCategory_path = BASE_DIR + '/maindata/static/maindata/pearentsCategory/pearentsCategory.txt'
        # 各ディレクトリのパス（固定値）
        self.img_dir = BASE_DIR + '/maindata/static/maindata/Upload_image/'
        self.model_dir = BASE_DIR + '/maindata/static/maindata/model/'
        self.category_json_dir = BASE_DIR + '/maindata/static/maindata/category_json/'
        self.category_text_dir = BASE_DIR + '/maindata/static/maindata/category_text/'
        # 各ファイルのパス（変動）
        self.img_path = ''
        self.model_json_path = ''
        self.model_h5_path = ''
        self.category_json_path = ''
        self.category_text_path = ''

    @property
    def img_path(self):
        return self.img_path

    @img_path.setter
    def img_path(self, file_name):
        self.img_path = self.img_dir + file_name + '.jpg'

    @img_path.deleter
    def img_path(self):
        self.img_path = None

    @property
    def model_json_path(self):
        return self.model_json_path

    @model_json_path.setter
    def model_json_path(self, file_name):
        self.model_json_path = self.model_dir + file_name + '.json'

    @model_json_path.deleter
    def model_json_path(self):
        self.model_json_path = None

    @property
    def model_h5_path(self):
        return self.model_h5_path

    @model_h5_path.setter
    def model_h5_path(self, file_name):
        self.model_h5_path = self.model_dir + file_name + '.h5'

    @model_h5_path.deleter
    def model_h5_path(self):
        self.model_h5_path = None

    @property
    def category_json_path(self):
        return self.category_json_path

    @category_json_path.setter
    def category_json_path(self, file_name):
        self.category_json_path = self.category_json_dir + file_name + '.json'

    @category_json_path.deleter
    def category_json_path(self):
        self.category_json_path = None

    @property
    def category_text_path(self):
        return self.category_text_path

    @category_text_path.setter
    def category_text_path(self, file_name):
        self.category_text_path = self.category_text_path + file_name + '.txt'

    @category_text_path.deleter
    def category_text_path(self):
        self.category_text_path = None

    @property
    def pearentsCategory_path(self):
        return self.pearentsCategory_path


class list(object):
    def __init__(self) -> object:
        self.category_dic = {}
        self.pearentsCategoryList = []
        self.all_category = []

    @property
    def pearentsCategoryList(self):
        return self.pearentsCategoryList

    @pearentsCategoryList.setter
    def pearentsCategoryList(self, value):
        pearents_path = path().pearentsCategory_path
        with open(pearents_path, 'r+', encoding='utf-8') as f:
            self.pearentsCategoryList = f.read().splitlines()

    @pearentsCategoryList.deleter
    def pearentsCategoryList(self):
        self.pearentsCategoryList = []

    @property
    def category_dic(self):
        return self.category_dic

    @category_dic.setter
    def category_dic(self, name):
        json_path = path().category_json_path(name)
        with open(json_path, 'r+', encoding='utf-8') as f:
            if __name__ == '__main__':
                self.category_dic = json.load(f)

    @category_dic.deleter
    def category_dic(self):
        self.category_dic = {}

    @property
    def all_category(self):
        return self.all_category

    @all_category.setter
    def all_category(self, name):
        text_path = path().category_text_path(name)
        with open(text_path, 'r+', encoding='utf-8') as f:
            self.all_category = f.read().splitlines()

    @all_category.deleter
    def all_category(self):
        self.all_category = []
