from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from aplicaciones.libro.forms import LibroForm
from aplicaciones.libro.models import Libro
# Create your views here.


def formulario_buscar(request):
	return render(request,'formulario_buscar.html')

def buscar(request):
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			errors.append('Por favor introduce un termino de busqueda.')
		elif len(q) > 20:
			errors.append('Por favor introduce un termino de busqueda menor a 20 caracteres')
		else:
			libros = Libro.objects.filter(titulo__icontains=q)
			return render(request, 'libro/resultados.html', {'libros':libros, 'query':q})

	return render(request, 'libro/formulario_buscar.html', {'errors':errors})









def index(request):
	return render(request, 'libro/index.html')

class LibroList(ListView):
	model = Libro
	template_name = 'libro/libro_list.html'
	queryset = Libro.objects.select_related('editor').all()


class LibroCreate(CreateView):
	model = Libro
	form_class = LibroForm
	template_name = 'libro/libro_form.html'
	success_url = reverse_lazy('libro:libro_listar_class')


class LibroUpdate(UpdateView):
	model = Libro
	form_class = LibroForm
	template_name = 'libro/libro_form.html'
	success_url = reverse_lazy('libro:libro_listar_class')


class LibroDelete(DeleteView):
	model = Libro
	template_name = 'libro/libro_delete.html'
	success_url = reverse_lazy('libro:libro_listar_class')







def libro_view(request):
	if request.method=='POST':
		form = LibroForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return redirect('libro:libro_listar_def')
	else:
		form=LibroForm()
	return render(request, 'libro/libro_form.html', {'form':form})

def libro_list(request):
	libro = Libro.objects.select_related('editor').all().order_by('id')
	contexto = {'libros':libro}
	return render(request, 'libro/libro_list.html', contexto)

def libro_edit(request, pk):
	libro = Libro.objects.get(id=pk) 
	if request.method == 'GET':
		form = LibroForm(instance=libro)
	else:
		form = LibroForm(request.POST, instance=libro)
		if form.is_valid():
			form.save()
		return redirect('libro:libro_listar_def')
	return render(request, 'libro/libro_form.html', {'form':form})

def libro_delete(request, pk):
	libro = Libro.objects.get(id=pk) 
	if request.method == 'POST':
		libro.delete()
		return redirect('libro:libro_listar_def')
	return render(request, 'libro/libro_delete.html', {'libro':libro})



