from django.db import models
from django.contrib.auth.forms import AuthenticationForm


class User(models.Model):
  login = models.CharField(max_length=50)
  password = models.CharField(max_length=50)

  def __str__(self):
      return self.login

  class Meta:
    managed = False



class CustomUser(models.Model):
  login = models.CharField(max_length=50, unique=True)
  password = models.CharField(max_length=50)

  def __str__(self):
    return self.login


class LoginForm(AuthenticationForm):
  login = models.CharField(max_length=50, unique=True)
  password = models.CharField(max_length=50)

  def __str__(self):
    return self.login


class Feedback(models.Model):
    """
    Модель обратной связи
    """
    subject = models.CharField(max_length=255, verbose_name='Тема письма')
    email = models.EmailField(max_length=255, verbose_name='Электронный адрес (email)')
    content = models.TextField(verbose_name='Содержимое письма')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')
    ip_address = models.GenericIPAddressField(verbose_name='IP отправителя', blank=True, null=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
      verbose_name = 'Обратная связь'
      verbose_name_plural = 'Обратная связь'
      ordering = ['-time_create']
      db_table = 'app_feedback'

    def __str__(self):
      return f'Вам письмо от {self.email}'


