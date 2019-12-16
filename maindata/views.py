from django.shortcuts import render
from django.http import HttpResponse


def genre_list(request):
    """ジャンルの一覧"""
    return HttpResponse('ジャンル一覧')