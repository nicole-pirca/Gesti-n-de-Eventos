from django.shortcuts import redirect, render

from contacto.models import Contacto

from .forms import FormularioContacto

from django.core.mail import EmailMessage
# Create your views here.
def contacto(request):
    
    formulario_contacto = FormularioContacto()

    if request.method == "post":
        formulario_contacto =FormularioContacto(data = request.post)
        if formulario_contacto.is_valid():
            nombre = request.post.get("nombre")
            email = request.post.get("email")
            contenido = request.post.get("contenido")

            email = EmailMessage("Mensaje desde App Django","El usuario con nombre {} con la direccion {} escribe lo siguiente : {}".format(nombre, email, contenido),
            "",["nicolepircaescobar@gmail.com"],reply_to=[email])

            try:
                email.send()

                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/invalido")

            return redirect("/contacto/?valido")
    return render(request,"contacto/contacto.html", {'miFormulario':formulario_contacto})
