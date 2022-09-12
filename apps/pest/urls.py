from django.urls import path
from apps.pest.views import PestView

urlpatterns = [
    path('pest/', PestView.as_view(), name='pest_list'),
    path('pest/<int:id>', PestView.as_view(), name='pest_process')
]
