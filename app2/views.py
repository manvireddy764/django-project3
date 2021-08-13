from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app2_fbv2(request):
    return HttpResponse('<h1 style="color:DodgerBlue;"><marquee>second fbv has created</marquee></h1>')