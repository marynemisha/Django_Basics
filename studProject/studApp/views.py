from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

# Create your views here.
class GoodMorningView(View):
    def get(self,request):
        data={
            "Message":"Good Morning...!"
             }
        return JsonResponse(data)
class HelloWorldView(View):
    def get(self,request):
        result={
               "Hello":"Introduction to Django",
               "Message":"Hello world..!"
              }
        return JsonResponse(result)
class GoodAfternoonView(View):
    def get(self,request):
        details={
                "Message":"Good Afternoon...!",
                 "Hello":"Had Lunch?"
        }
        return JsonResponse(details)
class GoodEvening(View):
    def get(self,request):
        res={
            "Message":"Good Evening..!"
        }
        return JsonResponse(res)