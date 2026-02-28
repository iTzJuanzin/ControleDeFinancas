from django.shortcuts import render, redirect
from django.contrib import messages
from .models import transacao
import pandas as pd
from django.http import HttpResponse

def home(request):
    transacoes = transacao.objects.all()
    saldo = 0
    total_entradas = 0
    total_saidas = 0

    for t in transacoes:
        if t.tipo == 'entrada':
            saldo += t.valor
            total_entradas += t.valor
        else: 
            saldo -= t.valor
            total_saidas += t.valor


    contexto = {
        'transacoes': transacoes, 
        'saldo': saldo, 
        'total_entradas': total_entradas, 
        'total_saidas': total_saidas,
    }

    return render(request, 'financas/home.html', contexto)



def adicionar(request):
    if request.method == 'POST':

        tipo = request.POST.get('tipo')
        descricao = request.POST.get('descricao')
        valor = request.POST.get('valor')


        if not descricao:
            messages.error(request, '❌ Digite uma descrição!')
            return redirect('home')
        try:
            valor = float(valor)
        except (ValueError, TypeError):
            messages.error(request, '❌ Valor inválido!')
            return redirect('home')
        
        if valor <= 0:
            messages.error(request, '❌ O valor deve ser positivo!')
            return redirect('home')
        
        transacao.objects.create(
            tipo = tipo, 
            descricao = descricao,
            valor = valor
        )
        
        messages.success(request, '✅ Transação registrada!' )

    return redirect('home')



def deletar(request, id):
    transacoes = transacao.objects.get(id=id)
    transacoes.delete()
    messages.success(request, '🗑️ Transação removida!')
    return redirect ('home')


def exportar_excel(request):
    
    transacoes = transacao.objects.all()

    dados = []
    for t in transacoes:
        data_formatada = t.data.strftime('%d/%m/%Y %H:%M')
        
        dados.append({
            'Data': data_formatada,
            'Tipo': t.tipo.upper(),  
            'Descrição': t.descricao,
            'Valor (R$)': float(t.valor) 
        })

    df = pd.DataFrame(dados)

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=extrato_financas.xlsx'

    df.to_excel(response, index=False)

    return response