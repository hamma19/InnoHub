from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template import RequestContext
from django.urls import reverse
from django.shortcuts import render

from.models import Project
from .forms import UserForm

def index(request):
    return HttpResponse("<h1> HELLO </h1>")

def errorExample(request):
    if True:
        return HttpResponseNotFound("<h1>404 NOT FOUND </h1>")

def home(request):
    return HttpResponse('<h1> Home Page </h1>')

def base(request):
    return render(request, 'firstapp/base.html')
def listProjets(request):
    project_list = Project.objects.all()
    return render(request, 'firstapp/projects.html', {'project_list': project_list})


def projectDetails(request, pId):
    project=get_object_or_404(Project, pk=pId)
    return render(request, 'firstapp/details.html', {'project': project})


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request,'firstapp/registration.html',
                          {'user_form':user_form,
                           'registered':registered})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'firstapp/login.html', {})
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def handler404(request, exception):
    context = RequestContext(request)
    err_code = 404
    response = render('404.html', {"code":err_code}, context)
    response.status_code = 404
    return response
