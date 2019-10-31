from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.

def index(request):
    return HttpResponse('genre 앱의 index 함수 실행')
def genreType(request, type):
    genre = ['ballade', 'dance', 'hiphop', 'rock', 'trot', 'pop', 'indie']
    if type in genre:
        return HttpResponse('genre 앱의 genreType 함수 실행')
    else:
        raise Http404('잘못된 요청입니다.')    

 