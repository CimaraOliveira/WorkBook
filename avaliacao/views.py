from django.shortcuts import render, redirect



def avaliacao(request):
    return render(request, 'avaliacao.html')

def avaliar(request):
    if request.POST['avaliacao']:
       descricao = request.POST['descricao']
       nota = request.POST['nota']

       avaliar = avaliacao.objects.create( decricao=descricao, nota=nota)
       avaliar.save()

       return redirect('usuario:submit_login')
