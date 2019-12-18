from django.urls import path, re_path
from maindata import views
from django.template.context_processors import csrf

app_name = 'maindata'
urlpatterns = [
    path('', views.top, name='top'),  # 一覧
    path('file_select/', views.file_select, name='file_select'),
    path('category/', views.category, name='category'),
    path('camera/', views.camera, name='camera'),
    path('file_select/sendfile/', views.send_file, name='imageCR'),
    re_path('result/', views.result, name='result'),

]
