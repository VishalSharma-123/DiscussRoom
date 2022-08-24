from django.shortcuts import render

room = [
    {'id': 1, 'name':'lets learn Python'},
    {'id': 2, 'name':'lets learn C++'},
    {'id': 3, 'name':'lets learn Java'},
]

#should be names as tempaltes/base

# triggerign rooms and home page
def home(request):
    context = {'rooms': room}
    return render(request, 'base/home.html', context)             #rendering the html file fromt template

def rooms(request, pk):
    rooms = None
    for i in room:
        if(i['id'] == int(pk)):
            room_s = i
    context = {'room': room_s}
    return render(request, 'base/room.html',context)
