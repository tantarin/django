from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Person


def index(request):
    return HttpResponse('Hello world')

def first(request):
    return HttpResponse('еще один текст')


def home(request):
    objects = Person.objects.all().delete()
    person = Person(first_name = "Tanya", last_name = "Ivanova")
    person.save()
    objects = Person.objects.all()
    res ='Printing all Persons entries in the DB :'
    for elt in objects:
        res += "Firs_name: "+elt.first_name
        res += "Last_name: "+elt.last_name
    return HttpResponse(res)



