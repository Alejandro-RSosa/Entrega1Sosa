from django.http import HttpResponse
from django.shortcuts import render
from appComida.models import Perros, Gatos, Snacks
from django.template import loader
from appComida.forms import Form_comida

# Create your views here.

def inicio(request):
    return render(request, "index.html")

def perros(request):
    perros = Perros.objects.all()
    dicc = {"perros" : perros}
    plantilla = loader.get_template("perros.html")
    doc = plantilla.render(dicc)
    return HttpResponse (doc)

def gatos(request):
    gatos = Gatos.objects.all()
    dicc = {"gatos" : gatos}
    plantilla = loader.get_template("gatos.html")
    doc = plantilla.render(dicc)
    return HttpResponse (doc)

def snacks(request):
    snackys = Snacks.objects.all()
    dicc = {"snacks" : snackys}
    plantilla = loader.get_template("snacks.html")
    doc = plantilla.render(dicc)
    return HttpResponse (doc)

def comida_perro(request):

    if request.method == "POST":

        mi_form = Form_comida( request.POST )

        if mi_form.is_valid():
            datos = mi_form.cleaned_data

            comida_perro = Perros(nombre=datos['nombre'], desc=datos['desc'], precio=datos['precio'])
            comida_perro.save()
            return render( request, "alta_perro.html")
    
    return render( request, "alta_perro.html")

def comida_gato(request):

    if request.method == "POST":

        mi_form = Form_comida( request.POST )

        if mi_form.is_valid():
            datos = mi_form.cleaned_data

            comida_gato = Gatos(nombre=datos['nombre'], desc=datos['desc'], precio=datos['precio'])
            comida_gato.save()
            return render( request, "alta_gato.html")
    
    return render( request, "alta_gato.html")

def comida_snacks(request):

    if request.method == "POST":

        mi_form = Form_comida( request.POST )

        if mi_form.is_valid():
            datos = mi_form.cleaned_data

            comida_snacks = Snacks(nombre=datos['nombre'], desc=datos['desc'], precio=datos['precio'])
            comida_snacks.save()
            return render( request, "alta_snacks.html")
    
    return render( request, "alta_snacks.html")

def buscar_comida(request):

    return render ( request, "buscar_comida.html")

def buscar(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        alimento = Perros.objects.filter(nombre__icontains = nombre)
        return render( request, "resultado_busqueda.html" , {"alimento" : alimento})
    else:
        return HttpResponse("No se encontro ese alimento")

