from django.urls import path, re_path, include
from maindata import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.template.context_processors import csrf

app_name = 'maindata'
urlpatterns = [
    path('', views.top, name='top'),  # 一覧
    path('file_select/', views.file_select, name='file_select'),
    path('camera/', views.camera, name='camera'),
    path('camera/result/', views.result, name='result'),
    path('file_select/result/', views.result, name='result'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
