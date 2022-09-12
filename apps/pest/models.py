from django.db import models
from apps.crop.models import Crop


# Create your models here.

class Pest(models.Model):
    name_pest = models.CharField(max_length=20)
    description_pest = models.TextField(max_length=500)
    photo_pest = models.ImageField(upload_to='image_pests')
    description_prevent= models.TextField(max_length=600)
    id_crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
