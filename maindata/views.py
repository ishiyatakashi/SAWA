from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.context_processors import csrf
from maindata.static.pyScript import requestPOST


def top(request):
    """top/タイトル一覧一覧"""
    return render(request, 'maindata/top.html')

def returns(request):
    """top/タイトル一覧一覧"""
    return HttpResponseRedirect("/")


def camera(request):
    return render(request, 'maindata/camera.html')


def file_select(request):
    return render(request, 'maindata/file_select.html')


def category(request):
    return render(request, 'maindata/category_select.html')


def result(request):
    site = 'maindata/result.html'
    # csrf対策
    c = {}
    c.update(csrf(request))

    if request.method == 'POST':
        if 'base64' not in request.POST:
            print("not file")
            return HttpResponseRedirect("/file_select")

    else:
        return HttpResponseRedirect("/")
    d = ai_work(request)
    return render(request, site, d)


def quiz_top(request):
    return render(request, 'maindata/.html')


def quiz_file(request):
    return render(request, 'maindata/file_select.html')


def quiz_camera(request):
    return render(request, 'maindata/camera.html')


def quiz_question(request):
    site = 'maindata/question.html'
    # csrf対策
    c = {}
    c.update(csrf(request))
    print(request.POST)
    print("BYMYBABY")
    if request.method == 'POST':
        if 'base64' not in request.POST:
            print("NOT FILE")
            return HttpResponseRedirect("/")

    else:
        return HttpResponseRedirect("/")
    d = ai_work(request)
    return render(request, site, d)


def quiz_answer(request):
    return render(request, 'maindata/answer.html')


def ai_work(request):
    ct = 0
    first = None
    send = requestPOST.requestPOST()
    result_list = send.study(request)
    first = max(result_list,key=result_list.get)
    d = {
        'first': first,
        'lists': result_list,
    }
    return d
