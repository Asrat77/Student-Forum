from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

rooms = [
    {'id': 1, 'name': 'Let us learn python'},
    {'id': 2, 'name': 'Web Development'},
    {'id': 3, 'name': 'Undergraduate Group'},
]


def room(request):
   return  render(request, 'room.html')
def home(request):
   context = {'rooms': rooms}
   
   return  render(request, 'home.html',context)
    