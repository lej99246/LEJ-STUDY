from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def blogIndex(request):
    return HttpResponse('blog 앱의 blogIndex 함수 실행')

def blogAdd(request):
    return HttpResponse('blog 앱의 blogAdd 함수 실행')

def blogUpdate(request, id):
    return HttpResponse('blog 앱의 blogUpdate 함수 실행')

def blogDelete(request, id):
    return HttpResponse('blog 앱의 blogDelete 함수 실행')

def blogView(request, id):
    return HttpResponse('blog 앱의 blogView 함수 실행')    

