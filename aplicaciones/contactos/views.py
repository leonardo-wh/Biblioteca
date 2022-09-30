from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from aplicaciones.contactos.forms import FormularioContactos
# Create your views here.

def contactos(request):
	if request.method=='POST':
		form=FormularioContactos(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			send_mail(
					cd['asunto'],
					cd['mensaje'],
					cd.get('email','leonardomartinxlr8@hotmail.com'), ['leonardomartinxlr8@hotmail.com']
				)
			return HttpResponseRedirect('gracias')
	else:
		form = FormularioContactos(initial={'asunto':'asuntooooo'})
	return render(request, 'contactos/formulario-contactos.html',{'form':form})



def gracias(request):
	return HttpResponse('gracias')

