from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_login(request):
    return HttpResponse("Hello, login here to access Task helper!")