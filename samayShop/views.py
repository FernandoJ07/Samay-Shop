from django.core import paginator
from django.db.models.query import InstanceCheckMeta
from django.shortcuts import render, redirect
from samayShop.models import Producto, Categoría
from django.contrib import messages
from django.core.paginator import Paginator
from samayShop.cart import Cart

# Create your views here.

def index(request):

    # Obtener categorías
    categorías = Categoría.objects.all()

    categoríaName = request.GET.get('categoría')

    if categoríaName and categoríaName != 'Todo':
        # Obtener productos de una categoría en específico
        instanciaCategoría = Categoría.objects.get(nombreCategoría = categoríaName)
        productos = Producto.objects.filter(categoría = instanciaCategoría)[0:4]
    else:
        # Obtener productos
        productos = Producto.objects.all()[0:4]


    return render(request, 'samayShop/index.html', {
        "productos": productos,
        'categorías': categorías
    })

def contacto(request):
    return render(request, 'samayShop/contacto.html')

def tienda(request):

    categorías = Categoría.objects.all()

    categoríaName = request.GET.get('categoría')

    if categoríaName and categoríaName != 'Todo':
        # Obtener productos de una categoría en específico
        instanciaCategoría = Categoría.objects.get(nombreCategoría = categoríaName)
        productos = Producto.objects.filter(categoría = instanciaCategoría)
    else:
        # Obtener productos
        productos = Producto.objects.all()

    paginator = Paginator(productos, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    return render(request, 'samayShop/tienda.html', {
        'categorías': categorías,
        "page_obj": page_obj

    })


def subirProducto(request):

    # Obtener información del formulario al ser enviado
    if request.method == "POST":
        nombre = request.POST['nombre']
        categoría = request.POST['categorías']
        precio = request.POST['precio']
        img = request.FILES['img']

        # Obtener una instancia del modelo categoría igual a la categoría seleccionada en el formulario
        instanciaCategoría = Categoría.objects.get(nombreCategoría = categoría)

        # guardar el productos con los datos del formularios procesador y redireccionar a index
        producto = Producto.objects.create(nombre = nombre, categoría = instanciaCategoría, precio = precio, img=img)
        producto.save()
        return redirect('index')

    # Monstar el formulario para ser rellenado y enviado
    else:
        categoríasSelect = Categoría.objects.all()
        return render(request, 'samayShop/subirProducto.html', {
            'categorías': categoríasSelect
        })

def detallesProducto(request, identificador):
    producto = Producto.objects.get(identificador = identificador)
    categoríasSelect = Categoría.objects.all()

    return render(request, 'samayShop/detallesProducto.html', {
        'producto': producto,
        'categorías': categoríasSelect

    })

def editarProducto(request, identificador):
    if request.method == 'POST':
        categoría = request.POST['categorías']

        instanciaCategoría = Categoría.objects.get(nombreCategoría = categoría)
        producto = Producto.objects.get(identificador = identificador)

        producto.nombre = request.POST['nombre']
        producto.categoría = instanciaCategoría
        producto.precio = request.POST['precio']
        if request.FILES.get('img') == None:
            pass
        else:
            producto.img = request.FILES['img']
        producto.save()

    return redirect('detallesProducto', identificador)

# def eliminarProducto(identificador):
#     producto = Producto.objects.get(identificador = identificador)
#     producto.delete()
#     return redirect('detallesProducto', identificador)

def crearCategoría(request):

    if request.method == "POST":
        categoría = request.POST['categoría']

        Categorías = Categoría.objects.filter( nombreCategoría = categoría).exists()
        if Categorías:
            messages.warning(request, "No puedes añadir categorías repetidas")
        else:
            instanciaCategoría = Categoría.objects.create( nombreCategoría = categoría)
            instanciaCategoría.save()
    return redirect('subirProducto')

def carrito(request):
    return render(request, 'samayShop/cart.html')


#Carrito de compras
def agregarProducto(request, identificador):
    cart = Cart(request)
    producto = Producto.objects.get(identificador = identificador)
    cart.add(producto)
    return redirect('carrito')

def eliminarProducto(request, identificador):
    cart = Cart(request)
    producto = Producto.objects.get(identificador = identificador)
    cart.remove(producto)
    return redirect('carrito')

def decrementarProducto(request, identificador):
    cart = Cart(request)
    producto = Producto.objects.get(identificador = identificador)
    cart.decrement(producto)
    return redirect('carrito')

def limpiarCarrito(request):
    cart = Cart(request)
    cart.clear()
    return redirect('carrito')
    
