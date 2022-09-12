from django.urls import path
from apps.user.views import UserView

# user urls creation
urlpatterns = [
    path('users/', UserView.as_view(), name='user_list'),
    path('users/<int:id>', UserView.as_view(), name='user_process')
]
