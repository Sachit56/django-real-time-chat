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

@login_required

def DetailRoomView(request,slug):
    room=RoomModel.objects.get(slug=slug)

    return render(request,'room/room.html',{
        'room':room
    })