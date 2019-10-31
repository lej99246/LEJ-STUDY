from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog

def blogIndex(request):
    data = Blog.objects.all()
    txt = ''
    txt += '<ul>'
    for d in data:
        txt += f'<li>{d.id} | <a href= "/blog/view/{d.id}/"> {d.title}</a> | {d.author}</li>'
    txt += "<ul>"
    return HttpResponse(txt)