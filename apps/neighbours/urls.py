from django.urls import path
from apps.neighbours.views import NeighbourView

urlpatterns = [
    path('neighbours/', NeighbourView.as_view(), name='neigh_list'),
    path('neighbours/<int:id>', NeighbourView.as_view(), name='neigh_process')
]
