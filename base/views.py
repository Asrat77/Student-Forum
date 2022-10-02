from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def room(request):
   return  render(request, 'room.html')
def home(request):
   return  render(request, 'home.html')
    