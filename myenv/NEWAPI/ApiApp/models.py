from django.db import models

# Create your models here.
class BookInfo(models.Model):
    Title = models.CharField(max_length=200)
    Code = models.CharField(max_length=500)
    Linenous = models.BooleanField()
    Language = models.CharField(max_length=200)
    Style = models.CharField(max_length=200)