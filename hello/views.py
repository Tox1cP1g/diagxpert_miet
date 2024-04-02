from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, "index.html")


def contacts(request):
    return render(request, "contacts.html")


def person(request):
    return render(request, "person.html")

@csrf_exempt
def postuser(request):
    # получаем из строки запроса имя пользователя  
    name = request.POST.get("name", "Undefined")
    age = request.POST.get("age", 1)
    langs = request.POST.getlist("languages", ["python"])

    return render(request, "person_result.html",
                 context={'name': name, 'age': age, 'langs': langs})





def picture(request):
    return render(request, "picture.html")