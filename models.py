from django.db import models

# Create your models here.
class User_book(models.Model):
    book_name=models.CharField(max_length=70)
    book_author=models.CharField(max_length=100)
