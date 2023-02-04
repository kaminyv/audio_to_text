from django.shortcuts import render
from .in_text import main

def index(request):
    text = main(request.GET.get('url'))
    response = dict(url=request.GET.get('url'), recognize_text=text)
    return render(request, 'index.html', response)
