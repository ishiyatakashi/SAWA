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
    print(request.POST['base64'])
    filename = 'request_image' + str(random.randint(1, 1000000000)) + '.jpg'
    # ファイルをバイナリから作る
    #binary = base64.b64decode(binary_image.splt(',')[1])
    binary = base64.b64decode("data:image/jpeg;base64,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"[1])
    img = Image.open(BytesIO(binary))
    # 保存場所の
    imgpass = BASE_DIR + '/maindata/static/maindata/Upload_image/' + filename
    # 保存する
    img.save(imgpass)
    return imgpass


def list_create(request):
    return request
