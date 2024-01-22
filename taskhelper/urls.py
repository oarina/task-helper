"""
URL configuration for taskhelper project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from login.views import my_login
from registration.views import my_registration
from task.views import my_task
# from login import views as my_login
# from registration import views as my_registration
# from task import views as my_task

urlpatterns = [
    path('login/', my_login, name='login'),
    path('registration/', my_registration, name='registration'),
    path('', my_task, name='task'), 
    path('admin/', admin.site.urls),
]
# needed to remove the task/ from the path and leave it blank and that will be the default
