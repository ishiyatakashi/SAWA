import shutil
import os
from PIL import Image
import sys
# import cv2
from django.core.files.storage import FileSystemStorage
from SAWA.settings import BASE_DIR

sys.path.append("/usr/local/lib/python2.7/site-packages")


def image_create(request):
    # html上のリクエスト上のファイルを呼ぶ
    request_file = request.FILES['file']
    # テンプレ文(初期値はMEDIA_ROOT)
    fileobject = FileSystemStorage()
    # ファイルの名前を指定(jpgファイル固定)
    filename = 'request_image.jpg'
    # ファイル保存()
    fileobject.save(filename, request_file)
    # 移動元
    upfile_pass = BASE_DIR + '/file/' + filename
    # 移動先
    move_pass = BASE_DIR + '/maindata/static/maindata/Upload_image/'
    # 移動
    shutil.move(upfile_pass, move_pass)
