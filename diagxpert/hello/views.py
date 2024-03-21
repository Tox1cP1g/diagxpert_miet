from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def contacts(request):
    return render(request, "contacts.html")


def person(request):
    return render(request, "person.html")


def postuser(request):
    # получаем из строки запроса имя пользователя
    name = request.POST.get("name", "Undefined")
    age = request.POST.get("age", 1)
    langs = request.POST.getlist("languages", ["python"])

    return HttpResponse(f"""
                <div>Name: {name}  Age: {age}<div>
                <div>Languages: {langs}</div>
            """)





def picture(request):
    return render(request, "picture.html")