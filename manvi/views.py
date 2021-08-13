from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def hello(request):
    return HttpResponse('this is vinod vinod is hansome')


def second(request):
    return HttpResponse('<h1><marquee>This is S N from FBV</marquee></h1>')    