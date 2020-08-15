from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tarea_ind
from .forms import Tarea_form, Raw_tarea_form
# Create your views here.

def Vista_tareas(request):
    
    tareas=Tarea_ind.objects.all()
    contexto={
    'tareas':tareas,

    }
    return render(request, 'listas.html', contexto)

def Vista_crear(request):
    error=""
    form=Tarea_form
    if request.method=='POST':
        form=Tarea_form(request.POST)
        if form.is_valid():
            form.save()
        else:
            error=form.errors.as_data()
        return redirect('/')
    contexto={
    'form':form,
    'error':error, 
    }
    return render(request, 'nueva_tarea.html', contexto)


def Vista_edicion(request, primary_key):
    
    tareas=Tarea_ind.objects.get(id=primary_key)
    form=Tarea_form(instance=tareas)
    if request.method=='POST':
        form=Tarea_form(request.POST, instance=tareas)
        if form.is_valid():
            form.save()
        else:
            print(form.errors.as_data())
    contexto={
        'form': form,
    }
    return render(request, 'editar_listas.html', contexto)


def Vista_eliminar(request, primary_key):
    tareas=Tarea_ind.objects.get(id=primary_key)

    if request.method=='POST':
        tareas.delete()
        return redirect('/')
    contexto={'tarea':tareas, 
              }
    return render(request, 'eliminar.html', contexto)
