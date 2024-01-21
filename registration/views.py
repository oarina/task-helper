from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_registration(request):
    return HttpResponse("Hello, register here to access Task helper!")