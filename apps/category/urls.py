from django.urls import path
from apps.category.views import CategoryView

urlpatterns = [
    path('categories/<int:id>', CategoryView.as_view(), name='categoria_process'),
    path('categories/', CategoryView.as_view(), name='categoria_list')
]