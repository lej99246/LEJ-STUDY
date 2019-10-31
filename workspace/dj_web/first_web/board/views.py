from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('board 앱의 index 함수 실행')

def add(request):
    return HttpResponse('board 앱의 add 함수 실행')

def update(request, id):
    return HttpResponse('board 앱의 update 함수 실행')

def delete(request, id):
    return HttpResponse('board 앱의 delete 함수 실행')

def view(request, id):
    return HttpResponse('board 앱의 view 함수 실행')

    