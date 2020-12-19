from django.shortcuts import render
from time import sleep

# Create your views here.
def index(request) :

    sleep(5)
    return render(request,'example/index.html')