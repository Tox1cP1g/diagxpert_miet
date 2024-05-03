from django.http import HttpResponse
# from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, FeedbackCreateForm
from .models import CustomUser, LoginForm, Feedback
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from hello.utils import get_client_ip
from hello.email import send_contact_email_message
from django.shortcuts import render
from newsapi import NewsApiClient
from news.models import Articles





# from django.http import HttpResponse
import sqlite3

# from static import css


def index(request):
    # context = get_context_data(request)
    # context['articles'] = Articles.objects.all()
    print(Articles.objects.all())
    articles = Articles.objects.all()
    for article in articles:
      print(f'Title: {article.title}')
      print(f'Body: {article.body}')
      print(f'Date: {article.date}')
      print('--------------------------')
    Articles.objects.all()
    context = {
        'articles': articles
    }
    # print(context)
    # context = super(Articles, self).get_context_data(**kwargs)                        
    # context['title'] = 'Заголовок страницы'
    # context['body'] = 'Содержимое страницы'
    # context['date'] = 'Дата обновления'
    # get_context_data(Articles.objects.all())
    return render(request, "index.html", {'username': request.user.username, 'articles': articles})


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
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('Login')
        password = request.POST.get('Password')
        print(login, password)
        try:
            user = CustomUser.objects.get(login=username, password=password)
            user = authenticate(request, custom_user=user, password=password)
            print(authenticate(request, custom_user=user, password=password))
            if user is None:
                login(request, user)
                print('Вход выполнен')
                return render(request, 'successfulauth.html')
        except ObjectDoesNotExist:
            print('ERROR')
            return render(request, 'auth_bad.html', {'error_message': 'User with this login does not exist.'})
    print('Без ошибки')
    return render(request, 'authorization.html')


# if request.method == 'POST':
  #   # {% csrf_token %}
  #   Login = request.POST.get('Login')
  #   Password = request.POST.get('Password')
  #   db_lp = sqlite3.connect('login_password.db')
  #   cursor_db = db_lp.cursor()
  #   cursor_db.execute(('''SELECT password FROM passwords
  #                                              WHERE login = '{}';
  #                                              ''').format(Login))
  #   pas = cursor_db.fetchall()
  #   cursor_db.close()
  #   try:
  #     if pas[0][0] != Password:
  #              return render(request, 'auth_bad.html')
  #   except:
  #          return render(request, 'auth_bad.html')
  #
  #   db_lp.close()
  #   return render(request, 'successfulauth.html')
  # return render(request, 'authorization.html')



@csrf_protect
def form_registration(request):
  if request.method == 'POST':
    # {% csrf_token %}
    Login = request.POST.get('Login')
    Password = request.POST.get('Password')
    print(Login, Password)
    user = CustomUser(login=Login, password=Password)
    user.save()
    return render(request, 'successfulregis.html')
  return render(request, 'registration.html')




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


class FeedbackCreateView(SuccessMessageMixin, CreateView):
    model = Feedback
    form_class = FeedbackCreateForm
    success_message = 'Ваше письмо успешно отправлено администрации сайта'
    template_name = 'feedback.html'
    extra_context = {'title': 'Контактная форма'}
    print('otpravleno')
    success_url = reverse_lazy('feedback')

    def form_valid(self, form):
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.ip_address = get_client_ip(self.request)
            feedback.User = self.request.user
            send_contact_email_message(feedback.subject, feedback.email, feedback.content, feedback.ip_address, feedback.user_id)
        return super().form_valid(form)


# Создание функции представления
def index1(request):

    newsapi = NewsApiClient(api_key ='02edf36d823544e8a1618643b7622f76')
    top = newsapi.get_top_headlines(sources ='techcrunch')

    l = top['articles']
    dsc =[]
    nws =[]
    im =[]

    for i in range(len(l)):
      f = l[i]
      nws.append(f['title'])
      dsc.append(f['description'])
      im.append(f['urlToImage'])
      mylist = zip(nws, dsc, im)

    return render(request, 'index1.html', context ={"mylist":mylist})

# def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     context['title', 'body', 'date'] = Articles.objects.all()

def my_view(request):
  # context = get_context_data(request)
  context['articles'] = Articles.objects.all()
  # print(Articles.objects.all(id=1))
  return render(request, 'index.html', context)

def get_context_data(self, **kwargs):
  context = super().get_context_data(**kwargs)
  context['title'] = 'Заголовок страницы'
  context['body'] = 'Содержимое страницы'
  context['date'] = 'Дата обновления'
  print(context)
  return context
