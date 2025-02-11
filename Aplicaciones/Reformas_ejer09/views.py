from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Cliente, Vivienda, ProyectoDeReforma, Material

#-----------------------------------------------------clientes------------------------------------------------------------
# Vista para la lista de clientes
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/listCliente.html', {'clientes': clientes})

# Vista para crear un nuevo cliente
def crear_cliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        foto = request.FILES.get('foto')  # Obtener el archivo de la imagen

        if Cliente.objects.filter(correo=correo).exists():
            messages.error(request, "El correo electrónico ya está registrado. Intenta con otro.")
            return redirect('crear_cliente')

        Cliente.objects.create(nombre=nombre, apellido=apellido, correo=correo, telefono=telefono, foto=foto)
        messages.success(request, "Cliente creado correctamente.")
        return redirect('lista_clientes')

    return render(request, 'clientes/addCliente.html')

# Vista para editar un cliente
def editar_cliente(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    if request.method == 'POST':
        cliente.nombre = request.POST.get('nombre')
        cliente.apellido = request.POST.get('apellido')
        cliente.correo = request.POST.get('correo')
        cliente.telefono = request.POST.get('telefono')

        if 'foto' in request.FILES:
            cliente.foto = request.FILES['foto']  # Actualiza la foto si se sube una nueva

        cliente.save()
        messages.success(request, "Cliente actualizado correctamente.")
        return redirect('lista_clientes')

    return render(request, 'clientes/upCliente.html', {'cliente': cliente})

# Vista para eliminar un cliente
def eliminar_cliente(request, pk):
    if request.method == 'POST':
        cliente = Cliente.objects.filter(pk=pk).first()
        if cliente:
            cliente.delete()
            messages.success(request, "Cliente eliminado correctamente.")
        else:
            messages.error(request, "El cliente no existe.")

    return redirect('lista_clientes')

#-----------------------------------------------------viviendas------------------------------------------------------------

# Vista para la lista de viviendas
def lista_viviendas(request):
    viviendas = Vivienda.objects.all()
    return render(request, 'viviendas/listVivienda.html', {'viviendas': viviendas})

# Vista para crear una nueva vivienda
def crear_vivienda(request):
    if request.method == 'POST':
        direccion = request.POST.get('direccion')
        tipo = request.POST.get('tipo')
        id_cliente = request.POST.get('id_cliente')
        foto = request.FILES.get('foto')  # Obtener la foto si se sube

        # Obtén el objeto Cliente por su ID
        cliente = Cliente.objects.get(id_cliente=id_cliente)

        # Crear una nueva vivienda asociada al cliente
        vivienda = Vivienda.objects.create(
            direccion=direccion,
            tipo=tipo,
            id_cliente=cliente,  # Asocias el cliente con la instancia del cliente
            foto=foto  # Guardamos la foto en el campo correspondiente
        )

        messages.success(request, "Vivienda creada correctamente.")
        return redirect('lista_viviendas')

    # Si es GET, pasamos la lista de clientes al formulario
    clientes = Cliente.objects.all()  # Obtener todos los clientes
    return render(request, 'viviendas/addVivienda.html', {'clientes': clientes})

# Vista para editar una vivienda
def editar_vivienda(request, pk):
    vivienda = Vivienda.objects.get(pk=pk)
    
    if request.method == 'POST':
        vivienda.direccion = request.POST.get('direccion')
        vivienda.tipo = request.POST.get('tipo')
        id_cliente = request.POST.get('id_cliente')

        # Obtén el objeto Cliente por su ID
        cliente = Cliente.objects.get(id_cliente=id_cliente)
        vivienda.id_cliente = cliente  # Asocia el cliente seleccionado

        # Si se sube una nueva foto, la reemplazamos
        if 'foto' in request.FILES:
            vivienda.foto = request.FILES['foto']  # Actualizamos la foto

        vivienda.save()
        messages.success(request, "Vivienda actualizada correctamente.")
        return redirect('lista_viviendas')

    # Si es GET, pasamos la vivienda y la lista de clientes
    clientes = Cliente.objects.all()  # Obtener todos los clientes
    return render(request, 'viviendas/updateVivienda.html', {'vivienda': vivienda, 'clientes': clientes})

# Vista para eliminar una vivienda
def eliminar_vivienda(request, pk):
    vivienda = Vivienda.objects.get(pk=pk)
    
    # Eliminar la foto del servidor cuando se elimina la vivienda
    if vivienda.foto:
        vivienda.foto.delete()

    vivienda.delete()
    messages.success(request, "Vivienda eliminada correctamente.")
    return redirect('lista_viviendas')





#-----------------------------------------------------proyectos------------------------------------------------------------

# Vista para la lista de proyectos de reforma
def lista_proyectos(request):
    proyectos = ProyectoDeReforma.objects.all()
    return render(request, 'proyectos/listProyecto.html', {'proyectos': proyectos})



def crear_proyecto(request):
    if request.method == 'POST':
        id_vivienda = request.POST.get('id_vivienda')
        estado = request.POST.get('estado')
        descripcion = request.POST.get('descripcion')
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')

        # Obtener la vivienda asociada por el ID
        vivienda = Vivienda.objects.get(id_vivienda=id_vivienda)

        # Crear un nuevo proyecto de reforma
        ProyectoDeReforma.objects.create(
            id_vivienda=vivienda,  # Asocia el proyecto a la vivienda seleccionada
            estado=estado,
            descripcion=descripcion,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin
        )

        messages.success(request, "Proyecto de reforma creado correctamente.")
        return redirect('lista_proyectos')

    # Si es GET, pasamos la lista de viviendas al formulario
    viviendas = Vivienda.objects.all()  # Obtener todas las viviendas
    return render(request, 'proyectos/addProyecto.html', {'viviendas': viviendas})


    # Si es GET, pasamos la lista de viviendas al formulario
    viviendas = Vivienda.objects.all()  # Obtener todas las viviendas disponibles
    return render(request, 'proyectos/addProyecto.html', {'viviendas': viviendas})

# Vista para editar un proyecto de reforma
def editar_proyecto(request, pk):
    proyecto = ProyectoDeReforma.objects.get(pk=pk)
    
    if request.method == 'POST':
        proyecto.direccion = request.POST.get('direccion')
        proyecto.tipo = request.POST.get('tipo')
        id_vivienda = request.POST.get('id_vivienda')
        proyecto.estado = request.POST.get('estado')
        proyecto.descripcion = request.POST.get('descripcion')
        proyecto.fecha_inicio = request.POST.get('fecha_inicio')
        proyecto.fecha_fin = request.POST.get('fecha_fin')

        # Obtener la vivienda asociada por el ID
        vivienda = Vivienda.objects.get(id_vivienda=id_vivienda)
        proyecto.id_vivienda = vivienda  # Asociamos la vivienda seleccionada

        proyecto.save()
        messages.success(request, "Proyecto de reforma actualizado correctamente.")
        return redirect('lista_proyectos')

    # Si es GET, pasamos el proyecto y la lista de viviendas
    viviendas = Vivienda.objects.all()  # Obtener todas las viviendas disponibles
    return render(request, 'proyectos/updateProyecto.html', {'proyecto': proyecto, 'viviendas': viviendas})

# Vista para eliminar un proyecto de reforma
def eliminar_proyecto(request, pk):
    proyecto = ProyectoDeReforma.objects.get(pk=pk)
    proyecto.delete()
    messages.success(request, "Proyecto de reforma eliminado correctamente.")
    return redirect('lista_proyectos')



#-----------------------------------------------------material------------------------------------------------------------

# Vista para la lista de materiales
def lista_materiales(request):
    materiales = Material.objects.all()  # Todos los materiales
    return render(request, 'materiales/listMaterial.html', {'materiales': materiales})

# Vista para crear un nuevo material

def crear_material(request):
    if request.method == 'POST':
        id_proyecto = request.POST.get('id_proyecto')
        nombre_material = request.POST.get('nombre_material')
        cantidad = request.POST.get('cantidad')

        # Obtener el proyecto de reforma seleccionado
        proyecto = ProyectoDeReforma.objects.get(id_proyecto=id_proyecto)

        # Crear el nuevo material
        Material.objects.create(
            id_proyecto=proyecto,
            nombre_material=nombre_material,
            cantidad=cantidad
        )

        messages.success(request, "Material creado correctamente.")
        return redirect('lista_materiales')

    # Si es GET, pasamos la lista de proyectos al formulario
    proyectos = ProyectoDeReforma.objects.all()  # Obtener todos los proyectos
    return render(request, 'materiales/addMaterial.html', {'proyectos': proyectos})


# Vista para editar un material
def editar_material(request, pk):
    material = Material.objects.get(id_material=pk)
    if request.method == 'POST':
        material.id_proyecto = ProyectoDeReforma.objects.get(id_proyecto=request.POST.get('id_proyecto'))
        material.nombre_material = request.POST.get('nombre_material')
        material.cantidad = request.POST.get('cantidad')
        
        material.save()
        messages.success(request, "Material actualizado correctamente.")
        return redirect('lista_materiales')

    proyectos = ProyectoDeReforma.objects.all()  # Obtener todos los proyectos
    # Verificar que el valor de cantidad se pasa correctamente
    print(f"Cantidad actual: {material.cantidad}")
    return render(request, 'materiales/updateMaterial.html', {'material': material, 'proyectos': proyectos})


# Vista para eliminar un material
def eliminar_material(request, pk):
    material = Material.objects.get(id_material=pk)
    material.delete()
    messages.success(request, "Material eliminado correctamente.")
    return redirect('lista_materiales')
