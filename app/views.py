from django.shortcuts import render
from .in_text import main


def index(request):
    if request.method == 'POST':
        text = main(request.POST.get('url'))
        response = dict(url=request.POST.get('url'), recognize_text=text)
        return render(request, 'index.html', response)
    return render(request, 'index.html', {})
