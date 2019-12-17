from PIL import Image
import sys
import cv2


sys.path.append("/usr/local/lib/python2.7/site-packages")


def image_create(request):
    image = cv2.imread(request.FILES['file'])
    cascade_path = cv2.CascadeClassifier('C:/Users/s20182089/AppData/Local/Continuum/anaconda3/Lib/site-packages/cv2'
                                         '/data/haarcascade_frontalface_default.xml')
    # 画像の保存先(フォルダに入れる場合最後にスラッシュ必須) 空白なら起動しているディレクトリです
    out_path = './image/'
    image_cnt = 1
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = cascade_path.detectMultiScale(gray, scaleFactor=1.45, minNeighbors=1, minSize=(32, 32))
    for (x, y, w, h) in faces:
        trim = image[y: y + h, x:x + w]
        # リサイズする（数字を変えると別のサイズにもできます）
        resize_image = cv2.resize(trim, (224, 224))
        # 画像を保存する（拡張子はOpenCVで使える型なら何でもいい）
        cv2.imwrite(out_path + 'cut' + str(image_cnt) + '.jpg', resize_image)
        image_cnt = image_cnt + 1


