from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def myfunction(request):
    return HttpResponse("Introduction to Django..!")

def demofunction(request):
    return HttpResponse("Welcome..!")