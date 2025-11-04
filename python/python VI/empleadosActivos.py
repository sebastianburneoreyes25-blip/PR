#Importamos librerias
from tabulate import tabulate

#Definimos variables
empleados=[{"Nombre":"Pepito", "Estado":"Activo"},{"Nombre":"Jacinta", "Estado":"Activo"},{"Nombre":"Roberto", "Estado":"Inactivo"},{"Nombre":"Alejandro", "Estado":"Inactivo"}]

#Definimos funciones
def statusEmpleado(lista):
    return lista["Estado"]=="Activo"

#Logica de programacion

empleadosActivos=list(filter(statusEmpleado, empleados))
print(tabulate(empleadosActivos, headers="keys", tablefmt="double_outline"))