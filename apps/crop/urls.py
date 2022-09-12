from django.urls import path
from apps.crop.views import CropView

urlpatterns = [
    path('crops/', CropView.as_view(), name='crop_list'),
    path('crops/<int:id>', CropView.as_view(), name='crop_process')
]
