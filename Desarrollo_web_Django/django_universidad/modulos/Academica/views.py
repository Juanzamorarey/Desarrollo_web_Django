from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def formularioContacto(request):
    return render(request, "formularioContacto.html")

def contactar(request):
    # Aquí vamos a coger los datos que necesitamos y redirigir a una página de éxito
    if request.method =="POST":
        # Primero almacenamos en variables los campos que ha usado el usuario:
        asunto = request.POST["txtAsunto"]
        mensaje = request.POST["txtMensaje"] + " / Email: " + request.POST["txtEmail"] #aquí indicamos también el email
        email_desde = settings.EMAIL_HOST_USER #Aquí importamos settings y cogemos nuestro correo desde el que se enviará la notificación
        email_para = ["juanzamorarey@gmail.com"] #Aquí debemos poner siempre una lista puesto que se puede enviar a más de un mail.
        send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)#Esta función también hay que importarla
        return render(request, "contactoExitoso.html")
    else:
        return render(request, "formularioContacto.html")
    