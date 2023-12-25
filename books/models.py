from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    available_for_borrow = models.BooleanField(default=True)
