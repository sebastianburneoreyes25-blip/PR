#Importamos librerias
from tabulate import tabulate

#Definimos variables
tareas=[{"Tarea":"Tarea 1", "Estado":"Urgente"},{"Tarea":"Tarea 1", "Estado":"Pendiente"},{"Tarea":"Tarea 5", "Estado":"Pendiente"},{"Tarea":"Tarea 8", "Estado":"Urgente"},{"Tarea":"Tarea 2", "Estado":"Urgente"}]

#Definimos funciones
def urgente(lista):
    return lista["Estado"]=="Urgente"

#Logica de programacion
tareasUrgentes=list(filter(urgente,tareas))
print(tabulate(tareasUrgentes, headers="keys", tablefmt="pretty"))