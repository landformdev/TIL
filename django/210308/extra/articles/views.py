from django.shortcuts import render
from datetime import datetime

def index(request):
    
    context = {

    }
    return render(request, 'index.html')


def hello(request):
    name = 'jojo'

    context = {
        'name' : name,
        'datetime': datetime.now()
    }
    return render(request, 'hello.html', context)


#variable routing example
def title(request, title, number):
    context = {
        'title': title,
        'number': number,
    }

    return render(request, 'title.html', context)


def throw(request):
    return render(request, 'throw.html')

def catch(request):
    
    context = {
        'message': request.GET.get('message'),
        'greeting': request.GET.get('greeting')
    }
    return render(request, 'catch.html', context)
