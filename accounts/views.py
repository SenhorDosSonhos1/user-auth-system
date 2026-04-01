from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == "GET":
        return render(request, 'accounts/register.html')
    
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm_password')

    if not username.strip() or not email.strip() or not password:
        messages.error(request, 'Preencha todos os campos!!')
        return redirect("register")

    if password != confirm_password:
        messages.error(request, 'As senhas não coincidem!!')
        return redirect("register")
    
    if User.objects.filter(username = username).exists():
        messages.error(request, 'Nome de usúario já existente!!')
        return redirect("register")
    
    user = User.objects.create_user(username = username,
                               email = email,
                               password = password
)
    
    messages.success(request, "Usuario cadastrado com sucesso!!")
    return redirect("login")

def user_login(request):
    if request.method == "GET":
        return render(request, 'accounts/login.html')
    
    username = request.POST.get("username")
    password = request.POST.get("password")

    if not username or not password:
        messages.error(request, 'Preencha todos os campos!!')
        return redirect("login")
    
    user = authenticate(request, username = username, password = password)

    if user is not None:
        login(request, user)
        #RETORNAR PRA UMA AREA RESTRITA COM O LOGIN REQUIRED
        return HttpResponse("Vocé está logado!!")

    else:
        messages.error(request, 'Credenciais inválidas!!')
        return redirect("login")
    
def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect("register")
    
    return redirect("login")