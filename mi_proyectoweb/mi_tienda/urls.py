from django.urls import path
# --Mapeo por patterns con las views
# --posibilidad de pasar datos por url
# -- Importar todas las vistas de mi_tienda
from .import views

# -- Aquí se definen las URLs de nuestra tienda
# -- Metemos de momento sólo la principal (índice)

# -- Cada vez que se reciba el recurso "" en mi tienda, se llamará a la función
# -- index() definida en views.py. Además se le signa la etiqueta "index" (name)
# -- para que podamos referenciar esta vista desdenuestras plantillas .
# -- urlpatternsurlpatterns son regular expresions
# -- Vista pricipal (índice)
urlpatterns = [

    path('', views.index, name='index'),
    #-- URL de la nueva vista test1:
    path('test1/', views.test1, name='test1'),
    #-- URL de la nueva vista test2:
    path('test2/', views.test2, name='test2'),
    #--  Plantilla desde Fichero
    path('test3/', views.test3, name='test3'),
    #--sólo usando la función render()
    path('test4/', views.test4, name='test4'),
    #--srecursos estáticos
    path('test5/', views.test5, name='test5'),
    #-- ejecutamos list cuyo codigo lee los objetos de db y los envia en html
    #-- renderiza con template listado el objeto en db productos
    path('Show_products/', views.list, name='Show_products'),
    path('Show_pedido/', views.list_pedido, name='Show_pedido'),
    path('FalconSerie/', views.FalconSerie, name='FalconSerie'),

    path('formulario1/', views.formulario1, name='formulario1'),
    #Vista de recepción de datos
    path('recepcion1/', views.recepcion1, name='reception1')


]
