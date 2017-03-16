from django.shortcuts import render
from core.models import *
from django.http import HttpResponse, HttpResponseRedirect
from PIL import Image,ImageDraw,ImageFont
from math import ceil
import random
import os
import io as cStringIO
from datetime import datetime,timedelta
import hashlib
from django.core.files.storage import default_storage
import json
import time
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.db import connection
from django.utils import timezone
try:
    from functools import wraps
except ImportError:
    from django.utils.functional import wraps  # Python 2.4 fallback.
from django.utils.decorators import available_attrs
from django.views.decorators.http import require_http_methods
import urllib.parse
import urllib.request
import base64
def my_custom_sql(sql,*para):
    cursor = connection.cursor()

    cursor.execute(sql,*para)

    #cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
    row = cursor.fetchall()

    return row


def index(request):
    '''
    首页
    '''

    return render(request, 'web/index.html', locals())


def education(request):
    '''
    教育咨询
    '''

    return render(request, 'web/education.html', locals())


def course(request):
    '''
    课程辅导
    '''

    return render(request, 'web/course.html', locals())


def aboutus(request):
    '''
    关于我们
    '''

    return render(request, 'web/Aboutus.html', locals())


def industry(request):
    '''
    行业咨询
    '''

    return render(request, 'web/industry.html', locals())
# def authourized(permission='',uid=''):
#     """
#     Decorator to make a view only accept particular authorized user.  Usage::
#
#
#
#     Note that request methods should be in uppercase.
#     """
#
#     def decorator(func):
#         @wraps(func, assigned=available_attrs(func))
#         def inner(request, *args, **kwargs):
#             userid=''
#             try:
#                 if uid == '':
#                     userid = request.session.get('userid', '0')
#
#                 perms = []
#                 relid=uid if uid !='' else userid
#                 if USER.objects.get(id=relid).Cpnid=='SYS':
#                     return func(request,*args, **kwargs)
#                 ret = my_custom_sql(
#                     r" select concat((select Name from core_app a where a.id = (select Appid_id from core_mdl m where f.mdl_id=m.id)),'.',(select Name from core_mdl m where f.mdl_id=m.id),'.',codename) as codename  from core_mdlfuncs f where mdl_id in (select grp.mdlid from core_cpngrppwr grp where grp.cpngrpid in (select up.Cpngrpid from core_usergrp up where up.Usrid in  (select u.id from core_user u where u.id=%s) ))",relid)
#                 for row in ret:
#                     perms.append(row[0])
#                 if permission in perms:
#                     return func(request,*args, **kwargs)
#                 return HttpResponse('权限不够,请联系管理员添加! <a href="/index">返回首页</a>')
#             except Exception as e:
#                 return HttpResponse(str(e)+' <a href="/login">返回登录</a>')
#         return inner
#     return decorator


def edit_carousel(req):
    '''
    修改轮播设置。

    :param req:
    :return:
    '''
    if req.method=='GET':

        return render(req, 'backend/carousel.html')
    elif req.method=='POST':
        r = {}
        post_args = req.POST
        img = req.FILES
        try:
            c = carousel.objects.get(id=post_args.get('id'))
            c.title = post_args.get('title')

            c.link = post_args.get('link')
            c.caption = post_args.get('caption')
        except Exception as e:
            r['msg'] = 'object not exist.due to \n %s' % ( str(e))
            r['status'] = '500'
            return HttpResponse(json.dumps(r,ensure_ascii=False))

        try:
            r['msg'] = '%s saved.' % (c.title)
            r['status'] = '200'
            c.img = default_storage.save('core/static/uploads/carousel_' + str(c.id), img['img'])
            c.save()
            return HttpResponse(json.dumps(r))
        except Exception as e:
            r['msg'] = '%s failed saving.due to \n %s' % (c.title, str(e))
            r['status'] = '500'
            return HttpResponse(json.dumps(r,ensure_ascii=False))
def add_carousel(req):
    r = {}
    post_args=req.POST
    img=req.FILES
    c=carousel()
    c.title=post_args.get('title')

    c.link = post_args.get('link')
    c.caption = post_args.get('caption')
    try:
        r['msg']='%s saved.' % (c.title)
        r['status']='200'
        c.img = default_storage.save('core/static/uploads/carousel_'+str(c.title)+'.jpg',img['img'])
        c.save()
        return HttpResponse(json.dumps(r))
    except Exception as e:
        r['msg']='%s failed saving.due to \n %s' % (c.title,str(e))
        r['status'] = '500'
        return HttpResponse(json.dumps(r,ensure_ascii=False))
def del_carousel(req):
    try:
        r = {}
        post_args = req.POST
        c=carousel.objects.get(id=post_args.get('id'))
        c.delete()
        r['msg']='%s deleted.' % (c.title)
        os.remove(c.img)
        r['status']='200'
        return HttpResponse(json.dumps(r))
    except Exception as e:
        r['msg']='failed deleting.due to \n %s' % (str(e))
        r['status'] = '500'
        return HttpResponse(json.dumps(r,ensure_ascii=False))
def newcode():
    '''
    生成新的4位数的图片验证码
    :return:
    '''
    CODE_WIDTH=90
    CODE_HEIGHT=30
    background = (random.randrange(230, 255), random.randrange(230, 255), random.randrange(230, 255))
    im = Image.new('RGB', (CODE_WIDTH, CODE_HEIGHT), background)
    # create
    draw = ImageDraw.Draw(im)
    for i in range(random.randrange(6 - 2, 6)):
        line_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        xy = (
            random.randrange(0, int(CODE_WIDTH * 0.2)),
            random.randrange(0, CODE_HEIGHT),
            random.randrange(3 * int(CODE_WIDTH / 4), CODE_WIDTH),
            random.randrange(0, CODE_HEIGHT)
        )
        draw.line(xy, fill=line_color, width=int(25 * 0.1))
    j = int(25 * 0.3)
    k = int(25 * 0.5)
    x = random.randrange(j, k)  # starts point
    mp = hashlib.md5()
    s=str(timezone.now()).encode()
    mp_src = mp.update(s)
    mp_src = mp.hexdigest()
    rand_str = mp_src
    for i in rand_str:
        # 上下抖动量,字数越多,上下抖动越大
        m = int(len(rand_str))
        y = random.randrange(1, 3)

        if i in ('+', '=', '?'):
            # 对计算符号等特殊字符放大处理
            m = ceil(25 * 0.8)
        else:
            # 字体大小变化量,字数越少,字体大小变化越多
            m = random.randrange(0, int(45 / 25) + int(25 / 5))

        #font = ImageFont.truetype("/home/ubuntu/wpc/core/static/timesnewrome/times.ttf", 25 + int(ceil(m)))
        font = ImageFont.truetype("core/static/timesnewrome/times.ttf", 25 + int(ceil(m)))

        draw.text((x, y), i, font=font, fill=random.choice(['black','darkblue','red']))
        x += 25 * 0.9

    del x
    del draw
    buf =open('core/static/temp.png','wb')
    im.save(buf, 'png')
    buf.close()
    return rand_str[:4]

def refreshcode(request):
    try:
        request.session['veriCode']=newcode()
        return HttpResponse('1')
    except Exception as e:
        return HttpResponse(e)