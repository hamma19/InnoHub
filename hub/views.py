from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse,HttpResponseNotFound

def index(request):
    return HttpResponse("<h1> HELLO </h1>")

def errorExample(request):
    if True:
        return HttpResponseNotFound("<h1>404 NOT FOUND </h1>")

def home(request):
    return HttpResponse('<h1> Home Page </h1>')

def base(request):
    return render(request,'hub/base.html')


