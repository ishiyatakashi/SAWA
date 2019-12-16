from django.shortcuts import render


def top(request):
    """top/タイトル一覧一覧"""
    return render(request, 'maindata/top.html')


def camera(request):

    return render(request, 'maindata/camera.html')


def file_select(request):
    return render(request, 'maindata/file_select.html')


def category(request):
    return render(request, 'maindata/camera_index.html')


def result(request):
    return render(request, 'maindata/result.html')
