from datetime import datetime
from django.conf import settings
from django.shortcuts import render, HttpResponse, redirect, HttpResponsePermanentRedirect, reverse
from django.http import JsonResponse
import pymysql
from .selfsql import SelfSql
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.clickjacking import xframe_options_exempt, xframe_options_sameorigin, xframe_options_deny
import os
import time
import json
from django.forms import Form, fields, widgets
res = SelfSql()


def hello(requrst):
    """
    测试页
    :param requrst:
    :return:
    """
    # return HttpResponse('hello')
    results1 = {}
    results1['name'] = 'Mr.Zheng'
    return render(requrst, 'login.html', results1)


def login(request):
    """
    登陆页
    :param request:
    :return:
    """
    if request.method == 'POST':
        name = request.POST.get('user-name')
        password = request.POST.get('password')
        result = res.sel_sql_login(name)
        print(result)
        results = {}
        if result and result[0][0] == password:
            # request.session['username'] = name
            return redirect("/get_python/")
        else:
            results['data'] = '登陆失败'
            return render(request, 'login.html', results)
    else:
        return render(request, 'login.html')


"""
以下是六个分页
"""


def get_python(request):
    if request.method == 'GET':
        datas = res.sel_sql_news()
        return render(request, 'python.html', {'datas': datas})


def get_java(request):
    datas = [1, 2, 3, 4, 5]
    if request.method == 'GET':
        return render(request, 'java.html', {'datas': datas})


def get_c(request):
    datas = [1, 2, 3, 4, 5]
    if request.method == 'GET':
        return render(request, 'c.html', {'datas': datas})


def get_c_add(request):
    datas = [1, 2, 3, 4, 5]
    if request.method == 'GET':
        return render(request, 'c_add.html', {'datas': datas})


def get_h5(request):
    datas = [1, 2, 3, 4, 5]
    if request.method == 'GET':
        return render(request, 'h5.html', {'datas': datas})


def get_my(request):
    datas = [1, 2, 3, 4, 5]
    if request.method == 'GET':
        return render(request, 'index.html')


def get_data(request):
    datas = {}
    """
    获取数据库新闻数据
    :param request:
    :return:
    """
    datas['news'] = res.sel_sql_news()
    datas['text'] = res.sel_sql_text()

    return JsonResponse(datas)


def writer_text(request):
    """
    富文本页
    :param request:
    :return:
    """
    return render(request, 'writer_text.html')


@xframe_options_exempt
def upload_img(request):
    """
    文件上传
    :param request:
    :return:
    """
    # dir = request.GET.get('dir')
    # img = request.FILES.get('post_img')
    # img_dir = settings.SAVEIMG_DIRS + img.name
    # print(dir, img.chunks(), img_dir)
    #
    # with open(img_dir, 'wb')as f:
    #     for f_m in img.chunks():
    #         f.write(f_m)
    # print('sava is ok !')

    dic = {
        'error': 0,
        'url': '/static/imgs/1.jpg',
        'message': '错误了...'
    }

    return HttpResponse(json.dumps(dic))


def file_manager(request):
    """
    文件管理
    :param request:
    :return:
    """
    dic = {}
    root_path = '/Users/wupeiqi/PycharmProjects/editors/static/'
    static_root_path = '/static/'
    request_path = request.GET.get('path')
    if request_path:
        abs_current_dir_path = os.path.join(root_path, request_path)
        move_up_dir_path = os.path.dirname(request_path.rstrip('/'))
        dic['moveup_dir_path'] = move_up_dir_path + '/' if move_up_dir_path else move_up_dir_path

    else:
        abs_current_dir_path = root_path
        dic['moveup_dir_path'] = ''

    dic['current_dir_path'] = request_path
    dic['current_url'] = os.path.join(static_root_path, request_path)

    file_list = []
    for item in os.listdir(abs_current_dir_path):
        abs_item_path = os.path.join(abs_current_dir_path, item)
        a, exts = os.path.splitext(item)
        is_dir = os.path.isdir(abs_item_path)
        if is_dir:
            temp = {
                'is_dir': True,
                'has_file': True,
                'filesize': 0,
                'dir_path': '',
                'is_photo': False,
                'filetype': '',
                'filename': item,
                'datetime': time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(os.path.getctime(abs_item_path)))
            }
        else:
            temp = {
                'is_dir': False,
                'has_file': False,
                'filesize': os.stat(abs_item_path).st_size,
                'dir_path': '',
                'is_photo': True if exts.lower() in ['.jpg', '.png', '.jpeg'] else False,
                'filetype': exts.lower().strip('.'),
                'filename': item,
                'datetime': time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(os.path.getctime(abs_item_path)))
            }

        file_list.append(temp)
    dic['file_list'] = file_list
    return HttpResponse(json.dumps(dic))


def save_h5(request):
    data = {}
    centext = request.body
    nowtime = time.strftime("%Y%m%d%H%M%S")
    h5_dir = settings.SAVEH5_DIRS + nowtime
    with open(h5_dir+'.html', 'wb')as f:
        f.write(centext)

    if centext:
        print('收到页面信息！')
        data['message'] = "保存成功！"
    else:
        data['message'] = "保存失败！"

    return HttpResponse(json.dumps(data))


def openh5(request):
    return render(request, '1.html')

