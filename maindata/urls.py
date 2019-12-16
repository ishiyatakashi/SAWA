from django.urls import path
from maindata import views

app_name = 'maindata'
urlpatterns = [
    path('', views.top, name='top'),  # 一覧
    path('file_select/', views.file_select, name='file_select'),
    path('category/', views.category, name='category'),
    path('camera/', views.camera, name='camera'),
    path('result/', views.result, name='result'),

]
