from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def store_list(request):
    return HttpResponse('Hi store')
