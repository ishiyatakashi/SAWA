import shutil
import os
from PIL import Image
import sys
# import cv2
from django.core.files.storage import FileSystemStorage
from SAWA.settings import BASE_DIR

sys.path.append("/usr/local/lib/python2.7/site-packages")


def image_create(request):
    request_file = request.FILES['file']
    fileobject = FileSystemStorage()
    filename = 'request_image.jpg'
    fileobject.save(filename, request_file)
    upfile_pass = BASE_DIR + '/file/' + filename
    move_pass = BASE_DIR + '/maindata/static/maindata/Upload_image/'
    shutil.move(upfile_pass, move_pass)
