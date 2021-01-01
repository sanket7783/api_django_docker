from django.contrib import admin
from django.urls import path
from .views import EventList,EventDetails

urlpatterns = [
    path('', EventList.as_view(),name="event_list"),
    path('<int:pk>/', EventDetails.as_view(), name="event_details")
]