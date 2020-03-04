"""Webboke URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', view.login),
    path('get_python/', view.get_python),
    path('get_java/', view.get_java),
    path('get_c/', view.get_c),
    path('get_c_add/', view.get_c_add),
    path('get_h5/', view.get_h5),
    path('get_my/', view.get_my),
    path('get_data/', view.get_data),  #
    path('file_manager/', view.file_manager),  # 文件管理
    path('upload_img/', view.upload_img),   # 上传图片
    path('writer_text/', view.writer_text),        # 访问富文本页面
    path('save_h5/', view.save_h5),  # 保存页面
    path('openh5/', view.openh5),
    # path('index/', view.index),
]
