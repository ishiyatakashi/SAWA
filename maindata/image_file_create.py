import shutil

import cv2
import numpy as np
import base64
from PIL import Image
import sys
# import cv2
from django.core.files.storage import FileSystemStorage
from SAWA.settings import BASE_DIR, MEDIA_ROOT
import random

sys.path.append("/usr/local/lib/python2.7/site-packages")


def image_create(request):
    # html上のリクエスト上のファイルを呼ぶ
    request_file = request.POST['base64']
    # ファイルの名前を指定(jpgファイル固定)
    filename = 'request_image' + str(random.randint(1, 1000000000)) + '.jpg'
    # ファイル保存
    img_binary = base64.b64decode(request_file)
    dec_img = np.frombuffer(img_binary, dtype=np.uint8)
    img = cv2.imdecode(dec_img, cv2.IMREAD_COLOR)
    cv2.imwrite(BASE_DIR + '/file/' + filename, img)
    # 移動元
    upfile_pass = BASE_DIR + '/file/' + filename
    # 移動先
    move_pass = BASE_DIR + '/maindata/static/maindata/Upload_image/'
    # 移動
    shutil.move(upfile_pass, move_pass)
