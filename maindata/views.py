from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
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


def send_file(request):
    site = 'maindata/result.html'
    if request.method == 'POST':
        c = {
            'name': request.POST["name"]
        }

    else:

        return HttpResponseRedirect("/")

    c.update(csrf(request))
    return render(request, site, c)
