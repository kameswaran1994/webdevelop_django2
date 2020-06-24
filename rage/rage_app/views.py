from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

def welcome(request):
    return HttpResponse("Hi How are you")

def date(request):
    return HttpResponse("The time is " +str(datetime.now()))

def about(request):
    return HttpResponse("I'm kamesh")
# Create your views here.
