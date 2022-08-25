from django.shortcuts import render
from .models import Room

# room = [
#     {'id': 1, 'name':'lets learn Python'},
#     {'id': 2, 'name':'lets learn C++'},
#     {'id': 3, 'name':'lets learn Java'},
# ]

#should be names as tempaltes/base

# triggerign rooms and home page
def home(request):
    room = Room.objects.all()
    context = {'rooms': room}
    return render(request, 'base/home.html', context)             #rendering the html file fromt template

def rooms(request, pk):
    room_s = Room.objects.get(id = pk)
    context = {'room': room_s}
    return render(request, 'base/room.html',context)
