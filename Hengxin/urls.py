"""Hengxin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from core import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', views.error, name="index"),
    url(r'^$', views.index, name="index"),
    url(r'^abroadeducation$', views.education, name="education"),
    url(r'^courseguide', views.courseguide, name="courseguide"),
    url(r'^highschool', views.highschool, name="highschool"),
    url(r'^mxztc', views.mxztc, name="mxztc"),
    url(r'^ksbk', views.ksbk, name="ksbk"),
    url(r'^aboutus', views.aboutus, name="aboutus"),
    url(r'^information', views.information, name="information"),
    url(r'^zygh', views.zygh, name="zygh"),
    url(r'^cydkzx', views.cydkzx, name="cydkzx"),
    url(r'^aboutus', views.aboutus, name="aboutus"),
    url(r'^information', views.information, name="information"),

    url(r'^(r/index|r)$', views.backend_index),
    url(r'^r/carousel$', views.edit_carousel),
    url(r'^r/addcarousel$', views.add_carousel),
    url(r'^r/delcarousel$', views.del_carousel),
    url(r'^r/getcarousel$',views.ajax_get_carousel),
    url(r'^r/gallery$',views.gallery),
    url(r'^r/getpictures$',views.ajax_get_pictures),
    url(r'^r/addpicture$',views.add_picture),
    url(r'^r/delpicture$',views.del_picture),
    url(r'^r/content$',views.content),
    url(r'^r/getcontent$', views.ajax_get_content),

    url(r'^r/editcontent$', views.edit_content),
    url(r'^r/filebrowser$', views.filebrowser),
    url(r'^r/login$', views.login_backend),
    url(r'^r/logout$', views.logout),
    url(r'^r/xxxuser$', views.add_user),
    url(r'^r/deluser$', views.del_user),
    url(r'^r/user$', views.edit_user),
    url(r'^r/getuser$', views.ajax_get_user),
    url(r'^misc/code$', views.refreshcode),
]
