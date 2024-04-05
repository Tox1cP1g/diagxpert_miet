from django.http import HttpResponse
# from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .models import CustomUser


# from django.http import HttpResponse
import sqlite3

# from static import css


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
    comment = request.POST.get("comment", "No comment")


    return render(request, "person_result.html",
                 context={'name': name, 'age': age, 'langs': langs, 'comment': comment})





def picture(request):
    return render(request, "picture.html")





# @csrf_exempt
def form_authorization(request):
  if request.method == 'POST':
    # {% csrf_token %}
    Login = request.POST.get('Login')
    Password = request.POST.get('Password')
    db_lp = sqlite3.connect('login_password.db')
    cursor_db = db_lp.cursor()
    cursor_db.execute(('''SELECT password FROM passwords
                                               WHERE login = '{}';
                                               ''').format(Login))
    pas = cursor_db.fetchall()
    cursor_db.close()
    try:
      if pas[0][0] != Password:
               return render(request, 'auth_bad.html')
    except:
           return render(request, 'auth_bad.html')

    db_lp.close()
    return render(request, 'successfulauth.html')
  return render(request, 'authorization.html')



# @csrf_protect
# def form_registration(request):
#   if request.method == 'POST':
#     # {% csrf_token %}
#     Login = request.POST.get('Login')
#     Password = request.POST.get('Password')
#     db_lp = sqlite3.connect('login_password.db')
#     cursor_db = db_lp.cursor()
#     sql_insert = '''INSERT INTO passwords VALUES('{}','{}');'''.format(Login, Password)
#     cursor_db.execute(sql_insert)
#     db_lp.commit()
#     db_lp.commit()
#     cursor_db.close()
#     db_lp.close()
#     return render(request, 'successfulregis.html')
#   return render(request, 'registration.html')




def register_user(request):
  if request.method == 'POST':
      form = UserRegistrationForm(request.POST)
      if form.is_valid():
          user = form.save(commit=False)  # Создаем объект пользователя, но не сохраняем его в базу данных
          user.save(using='other_db')  # Сохраняем объект пользователя в другой базе данных
          return redirect('successfulregis.html')
  else:
      form = UserRegistrationForm()
  return render(request, 'auth_bad.html', {'form': form})

def registration_success(request):
  return render(request, 'successfulregis.html')

