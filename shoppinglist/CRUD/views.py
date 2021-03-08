from django.shortcuts import render, HttpResponseRedirect
from .models import Produtos
from .forms import ProductForm

def home(request):
    form = ProductForm(request.POST)
    notas = Produtos.objects.all()

    context = {
        'notas': notas,
        'form' : form
    }

    if request.method == 'POST' and form.is_valid:
        form.save()

    return render(request, 'CRUD/index.html/', context)

def deletItem(request, pk):
    item = Produtos.objects.get(pk=pk)
    item.delete()

    return HttpResponseRedirect('/')

def editItem(request, pk):
    item = Produtos.objects.get(pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ProductForm(instance=item)

    context = {
        'form': form, 
        'item': item
    }

    return render(request,'CRUD/edit.html', context)
