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

    url(r'^$', views.error, name="index"),
    url(r'^index$', views.index, name="index"),
    url(r'^r/carousel$',views.edit_carousel),
    url(r'^education$',views.education),
    url(r'^industry',views.industry),
    url(r'^aboutus',views.aboutus),
    url(r'^r/addcarousel$',views.add_carousel),
    url(r'^course$', views.course),

    url(r'^r/delcarousel$',views.del_carousel),
    url(r'^r/getcarousel$',views.ajax_get_carousel),
    url(r'^r/gallery$',views.gallery),
    url(r'^r/getpictures$',views.ajax_get_pictures),
url(r'^r/addpicture$',views.add_picture),
url(r'^r/delpicture$',views.del_picture),
]
