from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime

# Create your views here.
def index(request):
    context = {
        'current_date' : datetime.now()
    }
    return render(request, 'index.html', context)


def select(request):
    context = {
        'number' : '4'
    }     
    return render(request, 'select.html', context)


def result(request):
    context = {
        'message' : '추첨 결과입니다.'
    }     
    return render(request, 'result.html', context)