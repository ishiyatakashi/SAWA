from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template.context_processors import csrf
from maindata.static.pyScript import requestPOST


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
    return HttpResponse(render)


def result2(request):
    return render(request, 'maindata/result2.html')


def send_file(request):
    site = 'maindata/result.html'
    ct = 0
    first = None
    second = None
    # csrf対策
    c = {}
    c.update(csrf(request))
    print(request.POST)
    print("AAAAAAA")
    if request.method == 'POST':
        if 'base64' not in request.POST:
            print("not file")
            return HttpResponseRedirect("/file_select")

    else:
        return HttpResponseRedirect("/")
    send = requestPOST.requestPOST()
    result_list = send.study(request)
    for i in result_list.keys():
        if ct == 0:
            first = i
        elif ct == 1:
            second = i
        ct = ct + 1

    d = {
        'first': first,
        'second': second,
        'lists': result_list
    }
    return render(request, site, d)
