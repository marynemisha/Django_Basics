from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
# Create your views here.
class GoodMorningView(View):
    def get(self,request):
        data={
            "Message":"Good Morning...!"
        }
        return JsonResponse(data)
class LibraryView(View):
    def get(self,request):
        res={
              "Library":"Central Library",
              "Location":"Idukki",
              "Status":"Open",
              "Time":"10am to 5pm"
        }
        return JsonResponse(res)
class BookView(View):
    def get(self,request):
        result={
            "Book Name":"Django for beginners",
            "Author":"William S.Vincent",
            "Price":650,
            "publish":2002
        }
        return JsonResponse(result)
class StudentView(View):
    def get(self,request):
        details={
            "Name":"Anu",
            "Course":"Python Django Full Stack",
            "Batch":"June 2026",
            "Institute":"Luminar Technolab",
            "Place":"Ekm"
        }
        return JsonResponse(details)
class BooksView(View):
    def get(self,request):
        detail={
                "Books":[
                    "Python",
                    "Django",
                    "Java",
                    "React",
                    "MySQL"
                ]
               }
        return JsonResponse(detail)
class EmployeeView(View):
    def get(self,request):
        response={
            "id":12067,
            "Name":"Anakha",
            "Place":"Ernakulam",
            "Designation":"Software Engineer",
            "Contact":9874561230,
            "Experience":"Fresher",
            "Qualification":"MTech"
        }
        return JsonResponse(response)