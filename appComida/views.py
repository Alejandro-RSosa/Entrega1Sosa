from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
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

def elimina_perros(request, id):

    comida = Perros.objects.get(id=id)
    comida.delete()

    comida = Perros.objects.all()

    return render(request, "perros.html", {"perros":comida})
    
def elimina_gatos(request, id):

    comida = Gatos.objects.get(id=id)
    comida.delete()

    comida = Gatos.objects.all()

    return render(request, "gatos.html", {"gatos":comida})

def elimina_snacks(request, id):

    comida = Snacks.objects.get(id=id)
    comida.delete()

    comida = Snacks.objects.all()

    return render(request, "snacks.html", {"snacks":comida})

def editarP(request, id):

    comida = Perros.objects.get(id=id)

    if request.method == "POST":

        mi_form = Form_comida(request.POST)

        if mi_form.is_valid():

            datos = mi_form.cleaned_data
            comida.nombre = datos["nombre"]
            comida.desc = datos["desc"]
            comida.precio = datos["precio"]
            comida.save()

            comida = Perros.objects.all()

            return render(request, "perros.html", {"perros":comida})
    else:
        mi_form = Form_comida(initial={'nombre':comida.nombre, 'desc':comida.desc, 'precio':comida.precio})

    return render(request, "editar_perros.html", {"mi_form":mi_form, "comida":comida})

def editarG(request, id):

    comida = Gatos.objects.get(id=id)

    if request.method == "POST":

        mi_form = Form_comida(request.POST)

        if mi_form.is_valid():

            datos = mi_form.cleaned_data
            comida.nombre = datos["nombre"]
            comida.desc = datos["desc"]
            comida.precio = datos["precio"]
            comida.save()

            comida = Gatos.objects.all()

            return render(request, "gatos.html", {"gatos":comida})
    else:
        mi_form = Form_comida(initial={'nombre':comida.nombre, 'desc':comida.desc, 'precio':comida.precio})

    return render(request, "editar_gatos.html", {"mi_form":mi_form, "comida":comida})

def editarS(request, id):

    comida = Snacks.objects.get(id=id)

    if request.method == "POST":

        mi_form = Form_comida(request.POST)

        if mi_form.is_valid():

            datos = mi_form.cleaned_data
            comida.nombre = datos["nombre"]
            comida.desc = datos["desc"]
            comida.precio = datos["precio"]
            comida.save()

            comida = Snacks.objects.all()

            return render(request, "snacks.html", {"snacks":comida})
    else:
        mi_form = Form_comida(initial={'nombre':comida.nombre, 'desc':comida.desc, 'precio':comida.precio})

    return render(request, "editar_snacks.html", {"mi_form":mi_form, "comida":comida})