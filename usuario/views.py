from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

import usuario
from categoria.models import Categoria
from perfil.models import Perfil
from .models import Usuario
from django.contrib import auth
from django.core.mail import send_mail


# buscar categorias pelos ids informados no html
def get_categorias(request):
    categorias = []
    for key, value in request.POST.items():
        if key.find('categoria') >= 0:
            print(key, value)
            categoria = Categoria.objects.get(id=value)
            if categoria:
                categorias.append(categoria)
    return categorias


def index(request):
    return render(request, 'index.html')


# mostrar perfil
def indexProf(request, id):

    try:
        perf = Usuario.objects.get(perfil_id=id)
        if perf:
            return render(request, 'PerfilProfissional.html', {'ListPerfil': perf})
    except:
        return render(request,'PerfilProfissional.html')

def home(request):
    return render(request, 'home.html')


# buscando profissões pelo nome na tela home
def home_perfil(request):
    # query nativa
    query = "select * from perfil p inner join usuario u on(p.id = u.id)where p.nome = %s"
    List = None

    nome = request.GET.get('profissao')
    if nome:
        List = Perfil.objects.raw(query, [nome])

    return render(request, 'home.html', {'List': List})


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


# para evitar repeticao
def register(request):
    username = request.POST['username']
    email = request.POST['email']
    senha = request.POST['senha']
    cidade = request.POST['cidade']
    telefone = request.POST['telefone']

    return {"username": username, "email": email, "senha": senha, "cidade": cidade, "telefone": telefone,
            "perfil": prof(request)}


# Aqui controla a parte do profissional
def prof(request):
    if request.POST['user'] == 'profissional':
        name_prof = request.POST['profissao']
        descricao = request.POST['descricao']
        slogan = request.FILES.get('slogan')
        perfil = Perfil.objects.create(nome=name_prof, decricao=descricao, slogan=slogan)
        perfil.categorias.set(get_categorias(request))
        return perfil
    return None


def perfil(request):
    if request.method != 'POST':
        categorias = Categoria.objects.all()

        return render(request, 'perfil.html', {"categorias": categorias})
    user_request = register(request)
    username = user_request.get('username')
    email = user_request.get('email')
    senha = user_request.get('senha')
    cidade = user_request.get('cidade')
    telefone = user_request.get('telefone')
    perfil = user_request.get('perfil')

    user_db = Usuario.objects.filter(email=email)
    if not user_db:
        messages.success(request, 'Usuário Registrado com Sucesso!')

        new_user = Usuario.objects.create_superuser(username=username,
                                                    email=email, password=senha, cidade=cidade, telefone=telefone,
                                                    perfil=perfil)

        send_mail(
            'Sua Conta foi Criada!',
            '%s, Cadastro Realizado com Sucesso!' % username,
            'sistema.workbook.21@gmail.com',
            [email],
            fail_silently=False,
        )

        new_user.save()
    messages.error(request, 'Usuário já Registrado. Tente outro e-mail!')
    return redirect('usuario:submit_login')
