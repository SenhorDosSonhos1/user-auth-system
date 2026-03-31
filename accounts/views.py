from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
# Create your views here.

def register(request):
    if request.method == "GET":
        return render(request, 'accounts/register.html')
    
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm_password')

    if not username or not email or not password:
        return HttpResponse("Preencha todos os campos!!")

    if password != confirm_password:
        return HttpResponse("Senhas diferentes!")
    
    if User.objects.filter(username = username).exists():
        return HttpResponse("Usuario já existe!!")
    
    user = User.objects.create_user(username = username,
                               email = email,
                               password = password
                               )
  
    return JsonResponse(
        {'name': username,
         'email': email,
         })

def user_login(request):
    if request.method == "GET":
        return render(request, 'accounts/login.html')
    
    username = request.POST.get("username")
    password = request.POST.get("password")

    if not username or not password:
        return HttpResponse("Preencha todos os campos!!")
    
    user = authenticate(username = username, password = password)

    if user is not None:
        login(request, user)
        return HttpResponse("Vocé está logado!!")

    else:
        return HttpResponse("Credenciais inválidas!!")