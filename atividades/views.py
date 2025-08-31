from django.shortcuts import render, redirect, get_object_or_404
from .models import Atividade
from .forms import AdicionarAtividade, EditarAtividade
from datetime import timedelta

def atividades_pendentes_list(request):
    atividades = Atividade.objects.filter(status='pendente').order_by('data_criacao')
    if request.method == 'POST':
        form = AdicionarAtividade(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('atividades_pendentes')
    else:
        form = AdicionarAtividade()  
    return render(request, 'atividades/atividades_pendentes.html',
                  {'atividades': atividades,
                   'form': form})
def concluir_atividade(request, atividade_id):
    atividade = get_object_or_404(Atividade, id=atividade_id)
    atividade.status = 'concluida'
    atividade.save()
    return redirect('atividades_pendentes')

def excluir_atividade(request, atividade_id):
    atividade = get_object_or_404(Atividade, id=atividade_id)
    atividade.delete()
    return redirect('atividades_pendentes')

def adiar_atividade(request, atividade_id):
    atividade = get_object_or_404(Atividade, id=atividade_id)
    atividade.data_vencimento += timedelta(days=1)
    atividade.save()
    return redirect('atividades_pendentes')

def editar_atividade(request, atividade_id):
    atividade = get_object_or_404(Atividade, id=atividade_id)
    if request.method == 'POST':
        form = EditarAtividade(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            atividade.descricao = cd['Atividade']
            atividade.categoria = cd['categoria']
            atividade.save()
            return redirect('atividades_pendentes')
    else:
        form = EditarAtividade(initial={
            'Atividade': atividade.descricao,
            'categoria': atividade.categoria,
        })
    return render(request, 'atividades/editar_atividade.html', {'atividade': atividade, 'form': form})

def atividades_concluidas_list(request):
    atividades_concluidas = Atividade.objects.filter(status='concluida')
    return render(request, 'atividades/atividades_concluidas.html', {'atividades_concluidas': atividades_concluidas})

def adiar_atividade(request, atividade_id):
    atividade = get_object_or_404(Atividade, id=atividade_id)
    atividade.data_vencimento += timedelta(days=1)
    atividade.status = 'adiada'
    atividade.save()
    return redirect('atividades_pendentes')

def mover_para_atividades(request, atividade_id):
    atividade = get_object_or_404(Atividade, id=atividade_id)
    atividade.status = 'pendente'
    atividade.save()
    return redirect('atividades_pendentes')

def atividades_adiadas_list(request):
    atividades_adiadas_list = Atividade.objects.filter(status='adiada')
    return render(request, 'atividades/atividades_adiadas.html', {'atividades_adiadas_list': atividades_adiadas_list})