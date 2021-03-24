from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Usuario
from django.contrib import auth



def index(request):
    return render(request, 'index.html')

def logout_user(request):
    logout(request)
    return redirect('submit_login')

def submit_login(request):
    if request.method != 'POST':
        return render(request, 'submit_login.html')

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = auth.authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('usuario:index')
    return redirect('usuario:submit_login')



def perfil(request):
    if request.method != 'POST':
        return render(request, 'perfil.html')
    username = request.POST['username']
    #first_name = request.POST['first_name']
    #last_name = request.POST['last_name']
    email = request.POST['email']
    senha = request.POST['senha']
    cidade = request.POST['cidade']
    telefone = request.POST['telefone']
    #password1 = request.POST['password1']

    messages.success(request, 'Usuário Registrado com Sucesso!')

    new_user = Usuario.objects.create_superuser(username=username,
                         email=email, password=senha, cidade=cidade, telefone=telefone)
    new_user.save()

    return redirect('usuario:submit_login')


