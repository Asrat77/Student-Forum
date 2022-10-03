from turtle import update
from unittest.util import _MAX_LENGTH
from django.db import models
from django.http import HttpResponse
# Create your models here.


class Room(models.Moedel):
    # host= 
    # topic=
    # participants=
    
    name = models.CharField(max_Length=200)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

