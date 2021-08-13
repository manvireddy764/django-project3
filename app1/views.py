from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app1_fbv1(request):
    return HttpResponse('<h1>first app1 has created</h1>')
