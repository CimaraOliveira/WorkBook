from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect

from avaliacao.models import Avaliacao
from usuario.models import Usuario

# funcao que retorna o usuario logado

def _request_user(request):
    try:
        user = Usuario.objects.get(id=request.user.id)
        if user:
            return user
    except Exception as err:
        print(err)
    return None
# funcao que retorna o perfil pelo id

def _request_perfil(id):
    try:
        prof = Usuario.objects.get(id=id)
        if prof.perfil:
            return prof
    except Exception as err:
        print(err)
    return None

def avaliacao(request, id):
    return render(request, 'avaliacao.html', {'perfil': _request_perfil(id)})


def avaliar(request, id):

    if request.POST['descricao']:
       client = _request_user(request)
       prof = _request_perfil(id)
       descricao = request.POST['descricao']
       nota = request.POST['fb']
       if client and prof:
            avaliar = Avaliacao.objects.create(descricao=descricao, nota=nota, cliente=client, proficional=prof)
            avaliar.save()

       return redirect('usuario:index')
    return avaliacao(request)

@login_required(login_url='usuario:submit_login')
def listAvaliacao(request):
    avaliar = Avaliacao.objects.filter(proficional=request.user.id)

    return render(request, 'ListAvaliacao.html', {'avaliar': avaliar})