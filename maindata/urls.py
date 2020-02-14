from django.urls import path,re_path
from maindata import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.template.context_processors import csrf

app_name = 'maindata'
urlpatterns = [
    path('', views.top, name='top'),  # 一覧
    re_path(r'top/', views.returns,name='top_return'),  # 一覧
    path('file_select/', views.file_select, name='file_select'),
    path('camera/', views.camera, name='camera'),
    path('camera/result/', views.result, name='result'),
    path('file_select/result/', views.result, name='result'),
    # 以下クイズモード
    path('q_file_select/', views.quiz_file, name='quiz_file'),
    path('q_camera/', views.quiz_camera, name='quiz_camera'),
    path('q_file_select/q', views.quiz_question, name='question'),
    path('q_camera/q', views.quiz_question, name='question'),
    path('q_file_select/answer', views.quiz_answer, name='answer'),
    path('q_camera/answer', views.quiz_answer, name='answer'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
