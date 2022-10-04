from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

from base.models import Room
# Create your views here.

'''
rooms = [
    {'id': 1, 'name': 'Let us learn python'},
    {'id': 2, 'name': 'Web Development'},
    {'id': 3, 'name': 'Undergraduate Group'},
]
'''

def room(request, pk):
   
   room = Room.objects.get(id=pk)
   context = {'room': room}
   
   return  render(request, 'base/room.html', context)

def home(request):
   rooms = Room.objects.all()
   context = {'rooms': rooms}
   
   return  render(request, 'base/home.html',context)


def createRoom(request):
   context = {}
   return render(request, 'base/room_form.html', context)