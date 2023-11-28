from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    host = request.META['HTTP_HOST']
    user_agent = request.META['HTTP_USER_AGENT']
    addr = request.META['REMOTE_ADDR']
    path = request.path

    return HttpResponse(f''
                        f'<p>Host: {host}</p>'
                        f'<p>Path: {path}</p>'
                        f'<p>User-agent: {user_agent}<p>'
                        f'<p>Addr: {addr}<p>')

def ERROR(request):
    return HttpResponse('К сожалению произошла ошибка', status=400, reason='Incorrect name')

def user(request, name='Undefined', age='0'):
    return HttpResponse(f'<h2>Имя: {name} Возраст:{age}<h2>')