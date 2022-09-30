from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from aplicaciones.editor.forms import EditorForm
from aplicaciones.editor.models import Editor
# Create your views here.


class EditorList(ListView):
	model = Editor
	template_name = 'editor/editor_list.html'


class EditorCreate(CreateView):
	model = Editor
	form_class = EditorForm
	template_name = 'editor/editor_form.html'
	success_url = reverse_lazy('editor:editor_listar_class')


class EditorUpdate(UpdateView):
	model = Editor
	form_class = EditorForm
	template_name = 'editor/editor_form.html'
	success_url = reverse_lazy('editor:editor_listar_class')


class EditorDelete(DeleteView):
	model = Editor
	template_name = 'editor/editor_delete.html'
	success_url = reverse_lazy('editor:editor_listar_class')


def editor_view(request):
	if request.method=='POST':
		form = EditorForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return redirect('editor:editor_listar_def')
	else:
		form=EditorForm()
	return render(request, 'editor/editor_form.html', {'form':form})

def editor_list(request):
	editor = Editor.objects.all().order_by('id')
	contexto = {'editores':editor}
	return render(request, 'editor/editor_list.html', contexto)

def editor_edit(request, pk):
	editor = Editor.objects.get(id=pk) 
	if request.method == 'GET':
		form = EditorForm(instance=editor)
	else:
		form = EditorForm(request.POST, instance=editor)
		if form.is_valid():
			form.save()
		return redirect('editor:editor_listar_def')
	return render(request, 'libro/libro_form.html', {'form':form})

def editor_delete(request, pk):
	editor = Editor.objects.get(id=pk) 
	if request.method == 'POST':
		editor.delete()
		return redirect('editor:editor_listar_def')
	return render(request, 'editor/editor_delete.html', {'editor':editor})