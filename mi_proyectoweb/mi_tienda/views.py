from django.shortcuts import render
# Create your views here.
#-- recibe el request y contruye devuelbe  en string HttpResponse python
# --Dinamico al componerse segun el request
# -- Fichero mi_tienda/views.py
# --plantilla + contexto = respuesta
from django.http import HttpResponse

from random import randint
from django.template import Template, Context
from django.template.loader import get_template

#-- Importamos clase producto para renderizar con la plantilla
from mi_tienda.models import Producto
from mi_tienda.models import Pedido
# -- Vista principal de mi tienda
# -- El nombre de la vista puede ser cualquiera. Nosotros lo hemos
# -- llamado index, pero se podría haber llamado pepito
def index(request):

    numero = randint(0, 100)
    return render(request, 'index.html', {'numero':str(numero)})

def FalconSerie (request):
    return render(request, "FalconSerie.html", {})


#-- Generar la página desde cero, a partir de código HTML que tenemos en una
 #--cadena. En los lugares que nos interese introducimos la información que queramos

 #--El mensaje de respuesta lo construimos nosotros a partir de código HTML
 #--empotrado en cadenas. Generamos una cadena con el párrafo con el número aleatorio
 #--y lo añadimos a la cadena original. Creamos otra cadena para completar el código HTML.

def test1(request):

    # -- Obtener el número aleatorio
    numero = randint(0, 100)
    # -- plantilla a fuego
    # Párrafo a insertar
    P = "<p>Numero aleatorio: " + str(numero) + " </p>"

    PAGINA_INI = """
    <!DOCTYPE html>
    <html lang="es" dir="ltr">
      <head>
        <meta charset="utf-8">
        <title>Test1</title>
      </head>
      <body>
        <h1>TEST1</h1>
    """

    PAGINA_FIN = """
      </body>
    </html>
    """
    return HttpResponse(PAGINA_INI + P + PAGINA_FIN)
     #--Y enviamos el mensaje de respuesta con el método HttpResponse

# -- Ejemplo de generacion mediante una plantilla en el código
def test2(request):

    # -- Obtener el número aleatorio
    numero = randint(0, 100)

    PLANTILLA = """
    <!DOCTYPE html>
    <html lang="es" dir="ltr">
      <head>
        <meta charset="utf-8">
        <title>Test2</title>
      </head>
      <body>
        <h1>TEST2</h1>
        <p> Numero aleatorio:  {{numero}} </p>
      </body>
    </html>
    """

    # --Procesar la plantilla
    t = Template(PLANTILLA)

    # -- Crear el contexto: Asignar el numero
    c = Context({'numero': str(numero)})

    # -- Obtener la pagina html final
    html = t.render(c)

    return HttpResponse(html)

#-- Generación con plantilla desde fichero
#-- La plantilla se lee desde el fichero, mediante la función get_template().
#-- Luego se aplica el contexto, se renderiza la página y se envía la respuesta

def test3(request):

    # -- Obtener el número aleatorio
    numero = randint(0, 100)

    # -- Leer la plantilla del fichero
    t = get_template('test.html')

    # -- Crear el contexto: Asignar el numero
    c = {'numero': str(numero)}

    # -- Obtener la pagina html final
    html = t.render(c)

    return HttpResponse(html)#--

# -- Ejemplo de uso de la función Render
def test4(request):
    # -- Obtener el número aleatorio
    numero = randint(0, 100)
    return render(request, 'test.html', {'numero':str(numero)})

#-- plantilla que utilice recursos estáticos.
def test5(request):
    # -- Obtener el número aleatorio
    numero = randint(0, 100)
    return render(request, 'test5.html', {'numero':str(numero)})

#--el codigo que construye una respuesta html con objetos de la db(sql)
def list(request):
    productos = Producto.objects.all()
    html = "<h2>Listado de articulos</h2>"
    for prod in productos:
        print(prod.nombre)
        html += '<p>'+ prod.nombre + ' ' + str(prod.precio) + '<p>'
    return HttpResponse(html)

#--el codigo que construye una respuesta html con objetos de la db(sql)
def list_pedido(request):
    pedido = Pedido.objects.all()
    html = "<h2>Listado Pedidos</h2>"
    for prod in pedido:
        print(prod.nombre)
        html += '<p>'+ prod.nombre + ' ' + str(prod.producto) + '<p>'
    return HttpResponse(html)

#pasamos plantilla y el render lo une con las variables productos,
#ejecutando listado.hmtl, renderiza con template listado el objeto en db productos

def Show_products(request):
    #-- busqueda en db con filtro de python,  cuyo modulo lo traduce leng sql
    #-- Producto.objects.all() devuelve todo en db
    productos = Producto.objects.all()
    return render(request, 'listado.html', {'productos':productos})



#vista que llamaremos formulario1 encargo en tienda,a través plantilla formulario1.hmtl
def formulario1(request):
    return render(request, 'formulario1.html', {})

#Vista de recepción de datos, lee los datos que han llegado del formulario.
#través del método POST, indicando el nombre del campo a leer. En ejemplo "nombre"
#mensaje respuesta con mini-pág web que confirma recibido  datos,y pone nombre recibido
def recepcion1(request):
    # -- Obtener el nombre de la persona
    persona = request.POST['nombre']
    producto = request.POST['nombre']
    # -- Imprimirlo en la consola del servidor
    print(f" PEDIDO RECIBIDO!!! ----> {persona}")
    return HttpResponse("Datos recibidos!!. Comprador: " + request.POST['nombre'])
