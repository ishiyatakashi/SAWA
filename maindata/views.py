from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template.context_processors import csrf
from maindata import image_file_create
from maindata import learning_resul


def top(request):
    """top/タイトル一覧一覧"""
    return render(request, 'maindata/top.html')


def camera(request):
    return render(request, 'maindata/camera.html')


def file_select(request):
    return render(request, 'maindata/file_select.html')


def category(request):
    return render(request, 'maindata/category_select.html')


def result(request):
    re = learning_resul
    parse, first, second = re.Study.select_learning()
    template = loader.get_template('maindata/result.html')
    return HttpResponse(render, template, {'first': first, 'second': second, 'lists': parse})


def result2(request):
    return render(request, 'maindata/result2.html')


def send_file(request):
    site = 'maindata/category_select.html'
    # csrf対策
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        None
        if 'base64' not in request.POST:
            print("not file")
            return HttpResponseRedirect("/file_select")
    else:

        return HttpResponseRedirect("/")
    image_file_create.image_create(request)
    return render(request, site)


def post(request):
