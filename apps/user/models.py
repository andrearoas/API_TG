from django.db import models


# Create your models here.
# User model creation

class User(models.Model):
    name_user = models.CharField(max_length=30)
    lastname_user = models.CharField(max_length=30)
    email_user = models.EmailField(max_length=50)
    password_user = models.CharField(max_length=30)
