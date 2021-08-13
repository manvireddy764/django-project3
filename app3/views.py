from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def app3_fbv3(request):
    return HttpResponse('<h1>this is the third fbv</h1>')