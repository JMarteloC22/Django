from django.shortcuts import render

def menu_vista(request):
    opciones = ['vehiculo', 'facturacion', 'proveedor', 'empleado', 'sede', 'conductor', 'gastos', 'administrador', 'puntos', 'premios']
    return render(request, 'parcial1/menu.html', {'opciones': opciones})
