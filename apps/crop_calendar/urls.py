from django.urls import path
from apps.crop_calendar.views import CropCalendarView

urlpatterns = [
    path('calendar/', CropCalendarView.as_view(), name='calendar_list'),
    path('calendar/<int:id>', CropCalendarView.as_view(), name='calendar_process')
]