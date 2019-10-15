from django.shortcuts import render
from django.http import HttpResponse


from .tasks import email

def index(request):
    email.delay(10)
    return HttpResponse('<h1>Email has been sent!</h1>')

