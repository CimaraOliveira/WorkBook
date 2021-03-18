from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Usuario


# Create your views here.
from django.views.decorators.csrf import csrf_protect
app_name = 'usuario'


def index_usurious(request):
    return render(request, 'index.html')

def logout_user(request):
    logout(request)
    return redirect('/login/')

def login_user(request):
    return render(request, 'login.html')

@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)



        if user is not None:
            login(request, user)
            return redirect('/login/#')
        else:
            messages.error(request, 'Usuário e senha inválido. Favor tentar novamente')
        return redirect('/index/')


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
    print(username)
    messages.success(request, 'Usuário Registrado com Sucesso!')

    new_user = Usuario.objects.create_superuser(username=username,
                         email=email, password=senha, cidade=cidade, telefone=telefone)
    new_user.save()

    return redirect('/login/#')