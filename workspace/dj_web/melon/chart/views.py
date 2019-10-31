from django.shortcuts import render
from django.http import HttpResponse, Http404
# Create your views here.

def index(request):
    return HttpResponse('chart 앱의 index 함수 실행')
def monthView(request, month=None):
    #1~12
    if month == None:
        return HttpResponse('chart 앱의 monthView 함수 실행 (1 ~ 12)')

    if month in tuple(range(1, 13)):
        return HttpResponse(f'chart 앱의 monthView 함수 실행 ({month})')
    else:  
        raise Http404('잘못된 요청 입니다.')  
def weekView(request, week=None):
        #1~52
    if week == None:
        return HttpResponse('chart 앱의 weekView 함수 실행 (1 ~ 52)')
        
    if week in tuple(range(1, 53)):
        return HttpResponse(f'chart 앱의 weekView 함수 실행 ({week})')
    else:  
        raise Http404('잘못된 요청 입니다.')  
    return HttpResponse('chart 앱의 weekView 함수 실행')
         