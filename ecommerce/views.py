from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, get_user_model
from .forms import LoginForm, RegisterForm

from django.template import RequestContext

def index(request):
    context = {
                    "title": "Home Page",
                    "content": "Bem vindo a Home Page",
              }
  
       
    return render(request, "index.html", context)


def logar(request):
    form = LoginForm(request.POST or None)
    context = {
                    "form": form
              }
   

    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password) 
        #print(user)
        
        if user is not None:
           
            login(request, user)
            print("Logado")
           
           #return redirect("api:index")
        else:
           
            print("Login falhou")
    return render(request, "login.html", context)

User = get_user_model()


def cadastrar(request):
    form = RegisterForm(request.POST or None)
    context = {
                    "form": form
              }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request, "cadastro.html", context)