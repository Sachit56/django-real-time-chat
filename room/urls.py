from django.urls import path
from . import views

app_name='room'

urlpatterns = [
    path('rooms/',views.RoomView,name='rooms')
]
