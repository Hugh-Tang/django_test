#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.shortcuts import render, HttpResponse
from utils.tencent.sms import send_sms_single
from web.forms.account import RegisterModelForm
from django_redis import get_redis_connection
import random
# Create your views here.


def send_sms(request):
    code = random.randrange(1000, 9999)
    res = send_sms_single('13485679617', 548760, [code, ])
    print(res)
    if res['result'] == 0:
        return HttpResponse('Success')
    else:
        return HttpResponse('errmsg')


def register(request):
    form = RegisterModelForm()
    return render(request, 'register.html', {'form': form})


def index(request):
    conn = get_redis_connection("default")
    conn.set('name', 'hugh', ex=10)
    value = conn.get('name')
    print(value)
    return HttpResponse("OK")
