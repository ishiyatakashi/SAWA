from django.http import HttpResponseRedirect
from django.shortcuts import render
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
    first = max(result_list,key=result_list.get)

    d = {
        'first': first,
        'lists': result_list
    }
    return render(request, site, d)
