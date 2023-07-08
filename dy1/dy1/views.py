from django.http import HttpResponse

def home(reqyest):
    return HttpResponse("hi am ovi")

def ad(reqyest):
    return HttpResponse("step2")