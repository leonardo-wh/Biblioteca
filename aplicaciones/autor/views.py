from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from aplicaciones.autor.forms import AutorForm
from aplicaciones.autor.models import Autor
# Create your views here.


class AutorList(ListView):
	model = Autor
	template_name = 'autor/autor_list.html'





class AutorCreate(CreateView):
	model = Autor
	form_class = AutorForm
	template_name = 'autor/autor_form.html'
	success_url = reverse_lazy('autor:autor_listar_class')


class AutorUpdate(UpdateView):
	model = Autor
	form_class = AutorForm
	template_name = 'autor/autor_form.html'
	success_url = reverse_lazy('autor:autor_listar_class')


class AutorDelete(DeleteView):
	model = Autor
	template_name = 'autor/autor_delete.html'
	success_url = reverse_lazy('autor:autor_listar_class')





def autor_view(request):
	if request.method=='POST':
		form = AutorForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return redirect('autor:autor_listar_def')
	else:
		form=AutorForm()
	return render(request, 'autor/autor_form.html', {'form':form})

def autor_list(request):
	autor = Autor.objects.all().order_by('id')
	contexto = {'autores':autor}
	return render(request, 'autor/autor_list.html', contexto)

def autor_edit(request, pk):
	autor = Autor.objects.get(id=pk) 
	if request.method == 'GET':
		form = AutorForm(instance=autor)
	else:
		form = AutorForm(request.POST, instance=autor)
		if form.is_valid():
			form.save()
		return redirect('autor:autor_listar_def')
	return render(request, 'autor/autor_form.html', {'form':form})

def autor_delete(request, pk):
	autor = Autor.objects.get(id=pk) 
	if request.method == 'POST':
		editor.delete()
		return redirect('autor:autor_listar_def')
	return render(request, 'autor/autor_delete.html', {'autor':autor})