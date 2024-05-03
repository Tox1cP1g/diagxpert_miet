from django.db import models

class Articles(models.Model):
  title = models.CharField(max_length = 120)
  body = models.TextField()
  date = models.DateTimeField()

  def _str_(self):
    return self.title
