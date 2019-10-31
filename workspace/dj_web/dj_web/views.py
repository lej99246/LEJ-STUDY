from django.http import HttpResponse

def first(request):
    return HttpResponse('First Page Resonpse')

def second(request):
    return HttpResponse('Second Page Response')

