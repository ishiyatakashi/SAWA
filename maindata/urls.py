from django.urls import path
from maindata import views

app_name = 'maindata'
urlpatterns = [
    # genre
    path('top/', views.genre_list, name='genre_list'),  # 一覧
]
