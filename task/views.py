from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_task(request):
    return HttpResponse("Hello, Task helper is here!")