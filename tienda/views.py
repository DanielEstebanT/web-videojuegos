from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Videojuego, Categoria
from .forms import CategoriaForm, VideojuegoForm

# Create your views here.


# Views pagina
def index(request):
    videojuegos = Videojuego.objects.all()  # Recuperamos todos los videojuegos
    return render(request, 'paginas/index.html', {'videojuegos': videojuegos})

def adminVideojuegos(request):
    videojuegos = Videojuego.objects.all()
    return render (request, "administrador/videojuegos.html", {'videojuegos': videojuegos})

def adminCategorias(request):
    categorias = Categoria.objects.all()
    return render (request, "administrador/categorias.html",{'categorias': categorias})

#Views categorias
def categorias(request):
    categorias = Categoria.objects.all() # aqui se llama o incluye todos los registros de libros
    return render (request, "categorias/index.html", {'categorias': categorias})

def crear_categoria(request):
    formulario = CategoriaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('admin-categorias')

    return render (request,'categorias/create.html', {'formulario': formulario})

def editar_categoria(request, id):
    categoria = Categoria.objects.get(id=id) #para recuperar datos
    formulario = CategoriaForm(request.POST or None, request.FILES or None, instance=categoria)
    if formulario.is_valid() and request.POST: #condicional para enviar datos
        formulario.save()
        return redirect('admin-categorias')
    return render (request, 'categorias/edit.html', {'formulario': formulario})

def eliminar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    if request.method == 'POST':  # Si el formulario se envía, procedemos a eliminar
        categoria.delete()
        return redirect('admin-categorias')  # Redirigimos al listado de categorías

    return render(request, 'categorias/confirmar_eliminacion_categoria.html', {'categoria': categoria})

#Views videojuegos

def videojuegos(request):
    videojuegos = Videojuego.objects.all()
    return render (request, "videojuegos/index.html", {'videojuegos': videojuegos})

def crear_videojuego(request):
    formulario = VideojuegoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid(): #condicional para enviar datos
        formulario.save()
        return redirect('admin-videojuegos')
    return render (request,'videojuegos/create.html', {'formulario': formulario})

def editar_videojuego(request, id):
    videojuego = Videojuego.objects.get(id=id)
    formulario = VideojuegoForm(request.POST or None, request.FILES or None, instance=videojuego)
    if formulario.is_valid() and request.POST: #condicional para enviar datos
        formulario.save()
        return redirect('admin-videojuegos')
    return render (request,'videojuegos/edit.html', {'formulario':formulario})

def eliminar_videojuego(request, id):
    videojuego = Videojuego.objects.get(id=id)
    if request.method == 'POST':  # Si el formulario se envía, procedemos a eliminar
        videojuego.delete()
        return redirect('admin-videojuegos')  # Redirigimos al listado de categorías

    return render(request, 'videojuegos/confirmar_eliminacion_videojuego.html', {'videojuego': videojuego})


def videojuegos_por_categoria(request, id):
    categoria = Categoria.objects.get(id=id)  # Obtenemos la categoría por ID
    videojuegos = Videojuego.objects.filter(categoria=categoria)  # Filtramos los videojuegos por esa categoría

    return render(request, 'videojuegos/index.html', {'categoria': categoria, 'videojuegos': videojuegos})

