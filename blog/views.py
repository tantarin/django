from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Person
from .forms import PersonForm


def index(request):
    tom = Person.objects.create(first_name="Tom", last_name="Ivanov")
    return render(request, "blog/create_person.html")

def first(request):
    return HttpResponse('еще один текст')


def create_post_page(request):
    if request.method == "POST":
        person = PersonForm(request.POST)
        if person.is_valid():
            person.save()

    form = PersonForm()
    context = {
        'form': form
    }
    return render(request, "blog/create_person.html", context)


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




