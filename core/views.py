from django.shortcuts import render


def index(request):
    '''
    首页
    '''

    return render(request, 'web/index.html', locals())

def edit_carousel(req):
    '''
    修改轮播设置。

    :param req:
    :return:
    '''
    return render(req,'backend/cpn.html')