from django.urls import path
from . import views

urlpatterns = [
    #------------------------------------------------------clientes------------------------------------------------------------
    path('', views.lista_clientes, name='lista_clientes'),  # Página de inicio
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/crear/', views.crear_cliente, name='crear_cliente'),
    path('clientes/editar/<int:pk>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/eliminar/<int:pk>/', views.eliminar_cliente, name='eliminar_cliente'),
    #------------------------------------------------------viviendas------------------------------------------------------------
    path('viviendas/', views.lista_viviendas, name='lista_viviendas'),  # Página que muestra la lista de viviendas
    path('viviendas/crear/', views.crear_vivienda, name='crear_vivienda'),  # Página para crear una nueva vivienda
    path('viviendas/editar/<int:pk>/', views.editar_vivienda, name='editar_vivienda'),  # Página para editar una vivienda
    path('viviendas/eliminar/<int:pk>/', views.eliminar_vivienda, name='eliminar_vivienda'),  # Página para eliminar una vivienda



    #------------------------------------------------------proyectos------------------------------------------------------------
    path('proyectos/', views.lista_proyectos, name='lista_proyectos'),  # Página que muestra la lista de proyectos de reforma
    path('proyectos/crear/', views.crear_proyecto, name='crear_proyecto'),  # Página para crear un nuevo proyecto de reforma
    path('proyectos/editar/<int:pk>/', views.editar_proyecto, name='editar_proyecto'),  # Página para editar un proyecto de reforma
    path('proyectos/eliminar/<int:pk>/', views.eliminar_proyecto, name='eliminar_proyecto'),  # Página para eliminar un proyecto de reforma


    #------------------------------------------------------materiales------------------------------------------------------------
    path('materiales/', views.lista_materiales, name='lista_materiales'),  # Página de lista de materiales
    path('materiales/crear/', views.crear_material, name='crear_material'),  # Página para crear un nuevo material
    path('materiales/editar/<int:pk>/', views.editar_material, name='editar_material'),  # Página para editar un material
    path('materiales/eliminar/<int:pk>/', views.eliminar_material, name='eliminar_material'),  # Página para eliminar un material
    
]
