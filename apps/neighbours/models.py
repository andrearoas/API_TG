from django.db import models
from apps.neighbours.choices import neighbour
from apps.crop.models import Crop


# neighbours model creation

class Neighbour(models.Model):
    type_neighbour = models.CharField(max_length=30, choices=neighbour, default='B')
    description_neigh = models.TextField(max_length=600)
    id_crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
