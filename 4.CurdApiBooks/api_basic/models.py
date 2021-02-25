from django.db import models

# Create your models here.

class Article(models.Model):
    bookname=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)
    price=models.IntegerField()
    avalaible=models.BooleanField(default=True)
def __str__(self):
    return self.bookname