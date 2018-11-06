from django.shortcuts import render, redirect # Nos sirve pare redireccionar
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.

def contact(request):
    # Obtenemos la plantillas desde el formulario
    contact_form = ContactForm

    # Validamos que la petición sea de tipo POST
    if request.method=="POST":
        # Rellenamos la plantilla con la información que está siendo enviada desde el form en el template
        contact_form=ContactForm(data=request.POST)
        # Validamos si los campos son correctos
        if contact_form.is_valid():
            # De ser correctos, que nos devuelva el valor con la clave name, de lo contrario, que nos devuelva una cadena vacía
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            # Suponemos que todo ha ido bien, redireccionamos
            # Pero, es una mala práctica pasar cadenas de texto en crudo, por que si la URL cambia, tendremos que cambiarla aquí también
            # return redirect('/contact/?ok') 
            # De esta manera, es como si tuviéramos un templatetag urls

            # Enviamos el correo y redireccionamos
            email = EmailMessage(
                "LA CAFFETTIERA: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["alienware.matrix@gmail.com"],
                reply_to=[email]
            )

            # Ahora, sólo nos queda enviar el email
            try:
                # Todo ha ido bien
                email.send()
                return redirect(reverse('contact')+'?ok')
            except:
                # Algo ha salido mal
                return redirect(reverse('contact')+'?fail')

    return render(request, "contact/contact.html", {'form':contact_form})