from django.http import HttpResponse
from django.template import loader

def nothing(request):
    template = loader.get_template('nothing/index.html')
    return HttpResponse(template.render(request))

def first(request):
    return HttpResponse('안녕하세요')

def second(request):
    return HttpResponse('안녕')    