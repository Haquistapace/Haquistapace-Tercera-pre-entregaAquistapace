from django.shortcuts import render
from .models import Deporte, Acreditacion, Socio
from AppHernan.forms import DeporteFormulario, BuscaDeporteForm
from AppHernan.forms import SociosFormulario
from AppHernan.forms import AcreditacionesFormulario


def inicio(request):
    return render(request, "AppHernan/index.html")

def profesores(request):
    return render(request, "AppHernan/socios.html")

def deportes(request):
    return render(request, "AppHernan/deportes.html")

def acreditaciones(request):
    return render(request, "AppHernan/acreditaciones.html")

def entregables(request):
    return render(request, "AppHernan/entregables.html")



def form_con_api(request):
    if request.method == "POST":
        miFormulario = DeporteFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            deporte = Deporte (deporte=informacion["deporte"], dia=informacion["dia"])
            deporte.save()
            return render(request, "AppHernan/index.html")
    else:
        miFormulario = DeporteFormulario()

    return render(request, "AppHernan/form_con_api.html", {"miFormulario": miFormulario})

def buscar_form_con_api(request):
    if request.method == "POST":
        miFormulario = BuscaDeporteForm(request.POST) # Aqui me llega la informacion del html

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            deportes= Deporte.objects.filter(deporte__icontains=informacion["deporte"])

            return render(request, "AppHernan/resultados_buscar_form.html", {"deportes": deportes})
    else:
        miFormulario = BuscaDeporteForm()

    return render(request, "AppHernan/buscar_form_con_api.html", {"miFormulario": miFormulario})

def mostrar_deportes(request):

    deportes = Deporte.objects.all() 

    contexto= {"deportes":deportes} 

    return render(request, "AppCoder/mostrar_deportes.html",contexto)

def deportes(request):
    if request.method == "POST":
        miFormulario = DeporteFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            deporte = Deporte(deporte=informacion["deporte"], dia=informacion["dia"])
            deporte.save()
            return render(request, "AppHernan/index.html")
    else:
        miFormulario = DeporteFormulario()

    return render(request, "AppHernan/form_con_api.html", {"miFormulario": miFormulario})


def acreditaciones(request):
    if request.method == "POST":
        miFormulario = AcreditacionesFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            acreditacion = Acreditacion(nombre=informacion["nombre"], apellido=informacion["apellido"],email=informacion["email"])
            acreditacion.save()
            return render(request, "AppHernan/index.html")
    else:
        miFormulario = AcreditacionesFormulario()

    return render(request, "AppHernan/form_con_api.html", {"miFormulario": miFormulario})


def socios (request):
    if request.method == "POST":
        miFormulario = SociosFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            socios = Socio(nombre=informacion["nombre"], apellido=informacion["apellido"],dni=informacion["dni"])
            socios.save()
            return render(request, "AppHernan/index.html")
    else:
        miFormulario = SociosFormulario()

    return render(request, "AppHernan/form_con_api.html", {"miFormulario": miFormulario})