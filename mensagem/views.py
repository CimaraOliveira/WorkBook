from django.shortcuts import render,get_object_or_404, redirect
from .models import Mensagem
from usuario.models import Usuario
from .forms import MensagemForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required(login_url='usuario:submit_login')
def enviarMensagem(request,id):
    usuario = get_object_or_404(Usuario, perfil_id=id)
    user = request.user.id
    form = MensagemForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('listarMensagem')
    else:
        form = MensagemForm(request.POST)

    context = {
        'form': form,
        'usuario': usuario,
        'user': user
    }
    return render(request, 'enviarMensagem.html', context)

@login_required(login_url='usuario:submit_login')
def listarMensagem(request):
    user = request.user.id
    mensagens = Mensagem.objects.filter(Q(destinatario=user) | Q(nomeRemetente=request.user.username))
    context = {
        'mensagens': mensagens,
        'user':user
    }
    return render(request, 'listarMensagem.html', context)


@login_required(login_url='usuario:submit_login')
def responderMensagem(request,remetente):
    respMensagem = Mensagem.objects.filter(remetente=remetente).first()
    user = request.user.id
    form = MensagemForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('listarMensagem')
    else:
        form = MensagemForm(request.POST)
    context = {
        'form': form,
        'respMensagem': respMensagem,
        'user': user
    }
    return render(request, 'responderMensagem.html', context)



