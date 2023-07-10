from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request , 'index.html')


def analysis(request):
    data=request.GET.get('mytext','default')
    chak=request.GET.get('chak','off')
    if chak =='on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        my_str = data
        no_punct = ""
        for char in my_str:
            if char not in punctuations:
                no_punct = no_punct + char
        par={'data':no_punct}
        return render(request, 'analysis.html',par)
    else:
        error="Please the chake box"
        pramiter={"error" : error}
        return render(request , 'index.html' ,pramiter)
