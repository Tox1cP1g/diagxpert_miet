from django.db import models


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

