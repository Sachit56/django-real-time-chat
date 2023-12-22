from django.urls import path
from . import views

app_name='room'

urlpatterns = [
    path('',views.RoomView,name='rooms'),
    path('<int:slug>/',views.DetailRoomView,name='room_detail')
]
