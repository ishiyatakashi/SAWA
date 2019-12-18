import shutil

from PIL import Image
import sys
import cv2
from django.core.files.storage import FileSystemStorage

sys.path.append("/usr/local/lib/python2.7/site-packages")


def image_create(request):
    request_file = request.FILES['file']
    fileobject = FileSystemStorage()
    imagefile = fileobject.save('request_image.jpg', request_file)



