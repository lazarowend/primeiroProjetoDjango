from django.shortcuts import render, redirect
from core.models import Produto
from .forms import ContatoForm, ProdutoModelForm
from django.contrib import messages 


def index(request):
    context = {
        'produtos': Produto.objects.all()
    }

    return render(request, 'index.html', context)

def contato(request):
    form = ContatoForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.send_mail()
            messages.success(request, 'Email enviado com successo!')
            form = ContatoForm()
            #return redirect(request, 'index')
        else:
            messages.success(request, 'Erro ao enviar email!')
        

    context = {
        'form': form
    }

    return render(request, 'contato.html', context)

def produto(request):
    print(f'usuario: {request.user}')
    if str(request.user) != 'AnonymousUser':
        if request.method == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():
                messages.success(request, 'Email enviado com successo!')
                prod = form.save(commit=True)
                print(f'{prod.nome},{prod.preco}, {prod.estoque}, {prod.img}')
                form = ProdutoModelForm()
        else:
            form = ProdutoModelForm()
        
        context = {
            'form': form
        }
        return render(request, 'produto.html', context)
    else:
        return redirect('index')

