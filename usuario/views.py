from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from rolepermissions.checkers import has_role
import usuario
from WorkBook.roles import Profissional
from WorkBook.roles import Usuario_Role
from categoria.models import Categoria
from perfil.models import Perfil
from .models import Usuario
from django.contrib import auth
from django.core.mail import send_mail
from .form import AlterUsuForm
from django.contrib.auth.decorators import login_required
from .models import FormDadosUsu

def sobre(request):
    return render(request, 'sobre.html')

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
def PerfilProf(request,id):
    try:
        user = Usuario.objects.get(id=id)
        if user.perfil:
            return render(request, 'PerfilProfissional.html', {'ListPerfil': user})
    except Exception as error:
        print(error)
    return render(request, 'PerfilProfissional.html')


def home(request):
    return render(request, 'home.html')


# buscando profissões pelo nome na tela home
'''def home_perfil(request):
    List = None

    nome = request.GET.get('profissao')
    if nome:
        List = Usuario.objects.filter(perfil__nome__contains=nome)

    return render(request, 'home.html', {'List': List})

#Buscando na tela index por serviço e cidade
def index_perfil(request):
    List = None

    nome = request.GET.get('profissao')
    cidade = request.GET.get('destino')

    if nome and cidade:
        List = Usuario.objects.filter((Q(cidade__contains=cidade))
                                      & (Q(perfil__nome__contains=nome))
                                      & (Q(perfil__isnull=False))
                                      )

    return render(request, 'index.html', {'List': List})'''

def is_user_logado(request):
    if request.user.username:
        return True
    return False

#Buscando na tela index por serviço e cidade
def index_perfil(request):
    List = None

    nome = request.GET.get('profissao')
    cidade = request.GET.get('destino')

    if is_user_logado(request):
        if nome and cidade:

            List = Usuario.objects.filter((Q(cidade__contains=cidade))
                                          & (Q(perfil__nome__contains=nome))
                                          & (Q(perfil__isnull=False))
                                          )

        return render(request, 'index.html', {'List': List})
    elif nome:
        List = Usuario.objects.filter(perfil__nome__contains=nome)
    return render(request, 'home.html', {'List': List})


def logout_user(request):
    request.session.flush()
    logout(request)
    return redirect('usuario:submit_login')


def submit_login(request):
    if request.method != 'POST':
        return render(request, 'submit_login.html')

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = auth.authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        messages.success(request, 'Login efetuado Sucesso!')
        return redirect('usuario:index')
    messages.error(request, 'E-mail e/ou senha inválido!')
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

def __get__register(request, user, error):
    categorias = Categoria.objects.all()
    return render(request, 'perfil.html', {"categorias": categorias, 'user': user, 'error': error})


def perfil(request):
    if request.method != 'POST':
        return __get__register(request, None, None)
    user_request = register(request)
    username = user_request.get('username')
    first_name = request.POST['first_name']
    email = user_request.get('email')
    senha = user_request.get('senha')
    cidade = user_request.get('cidade')
    telefone = user_request.get('telefone')
    perfil = user_request.get('perfil')

    user = {'username': username, 'first_name': first_name, 'email': email, 'senha': senha, 'telefone': telefone, 'perfil': request.POST['user']}

    user_db = Usuario.objects.filter(email=email)

    if not user_db:
        print('success')
        messages.success(request, 'Usuário Registrado com Sucesso!')

        new_user = Usuario.objects.create_superuser(username=username,first_name=first_name,
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
        return redirect('usuario:submit_login')
    print('error')
    return __get__register(request, user, {'error': 'Usuário já Registrado. Tente outro e-mail!'})

@login_required(login_url='usuario:submit_login')
def alterarUsuario(request, id):
    data = {}
    usuario = Usuario.objects.get(id=id)
    form = AlterUsuForm(request.POST or None, instance=usuario)

    if form.is_valid():
        form.save()
        messages.success(request, 'Dados alterados com Sucesso!')
        return redirect('usuario:index')

    data['form'] = form
    data['usuario'] = usuario
    return render(request, 'alterarUsuario.html',data)


@login_required(login_url='usuario:submit_login')
def detalhesusuario(request,id):
    data = {}
    usuario = Usuario.objects.get(id=id)
    form = FormDadosUsu(request.POST or None, instance=usuario)

    if form.is_valid():
        form.save()
        return redirect('disciplina:listar')

    data['form'] = form
    data['usuario'] = usuario
    return render(request, 'detalhesusuario.html', data)
