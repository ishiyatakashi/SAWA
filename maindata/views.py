from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.context_processors import csrf


def top(request):
    """top/タイトル一覧一覧"""
    return render(request, 'maindata/top.html')


def camera(request):

    return render(request, 'maindata/camera.html')


def file_select(request):
    return render(request, 'maindata/file_select.html')


def category(request):
    return render(request, 'maindata/category_select.html')


def send_file(request):
    site = 'maindata/result.html'
    if request.method == 'POST':
        c = {
            'name': request.POST["name"]
        }
        image_file_create.image_create(request)

    else:

        return HttpResponseRedirect("/")

    c.update(csrf(request))
    return render(request, site, c)
