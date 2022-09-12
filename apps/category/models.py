from django.db import models
from apps.category.choices import type_c


# Category model creation

class Category(models.Model):
    name_category = models.CharField(max_length=20)
    type_category = models.CharField(max_length=1, choices=type_c, default='1')
