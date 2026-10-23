from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.http import JsonResponse
# Create your views here.
def myfunction(request):
    return HttpResponse("Introduction to django...!")
def samplefunction(request):
    return HttpResponse("Welcome..!")
class GoodMorning(View):
    def get(self,request):
        data={
            "Message":"Good Morning..!"
        }
        return JsonResponse(data)
class GoodNight(View):
    def get(self,request):
        result={
            "Message":"Good Night...!"
        }
        return JsonResponse(result)