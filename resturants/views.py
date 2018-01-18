from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    #return HttpResponse("Hello from home")
    return render(request,'resturants/home.html')
