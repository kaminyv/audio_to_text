from django.shortcuts import render


def index(request):
    response = dict(url=request.GET.get('url'), recognize_text='Test')
    return render(request, 'index.html', response)
