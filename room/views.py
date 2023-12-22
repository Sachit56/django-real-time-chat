from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import RoomModel


# Create your views here.
@login_required
def RoomView(request):
    rooms=RoomModel.objects.all()
    return render(request,'room/rooms.html',{
        'rooms':rooms
    })