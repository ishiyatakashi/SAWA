import base64
from PIL import Image
import sys

from django.core.files.storage import FileSystemStorage
from SAWA.settings import BASE_DIR
import random
from io import BytesIO

sys.path.append("/usr/local/lib/python2.7/site-packages")


def image_create(request):
    binary_image = request.POST['base64']
    # 保存用のメソッド
    fileobject = FileSystemStorage()
    # ファイルの名前を作成
    filename = 'request_image' + str(random.randint(1, 1000000000)) + '.jpg'
    # ファイルをバイナリから作る
    binary = base64.b64decode(binary_image.splt(',')[1])
    img = Image.open(BytesIO(binary))
    # 保存場所の
    imgpass = BASE_DIR + '/maindata/static/maindata/Upload_image/' + filename
    # 保存する
    img.save(imgpass)

    return imgpass


def list_create(request):
    return request
