from django.conf.urls import url
from aplicaciones.contactos.views import contactos, gracias



urlpatterns = [

    url(r'^contactos/$', contactos, name="contactanos"),
    url(r'^contactos/gracias/$', gracias, name="gracias"),

]
