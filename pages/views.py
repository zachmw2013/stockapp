from django.shortcuts import render, redirect
from django.views.generic import TemplateView
import requests
import time
from twelvedata import TDClient
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import RegisterForm




# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class testPageView(TemplateView):
    template_name = 'test.html'

class loginpageview(TemplateView):
    template_name = 'login.html'

class RegisterPageView(TemplateView):
    template_name = 'register.html'


def index(request):
    return render(request, 'pages/home.html')

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        #return redirect('accounts/login')
    else:          
        form = RegisterForm()

    return render(response, "register.html", {"form":form})


def login(request):
    return render(request, 'login.html')




def button(request):

    return render(request, 'test.html')

#def input(request):
  # if response.method == 'GET':
   #    userinput = request.get("ticker")
   #return render(request,'test.html')

def output(request):
    if request.GET.get("ticker"):
        userinput = request.GET.get("ticker")
        td = TDClient(apikey="5ab205ca85414927b3b757076d329696")
        ts=td.time_series(symbol=userinput, interval="1min", outputsize=1).as_json()
        return render(request,'test.html',{'script':ts})