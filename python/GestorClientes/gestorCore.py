#Importamos librerias
import numpy as np
import pickle as pkl
from tabulate import tabulate
from pathlib import Path

#Definimos funciones
def mostrarMenu(menu):#Funcion para mostrar menu
    for i in menu:
        print(i)

def altaCliente(lista):#Funcion para dar de alta a un cliente
    cliente=[]
    dni=input("Escribe el dni del cliente\n")
    dni=dni.upper()
    dni=formatoDNI(dni)
    nombre=input("Escribe el nombre del cliente\n")
    apellidos=input("Escribe los apellidos del cliente\n")
    telefono=input("Escribe el telefono del cliente \n")
    telefono=esNumerico(telefono)
    if len(lista)==0:#Cuando la lista esté vacía no hará falta hacer ninguna comprobación de datos
        cliente.append(dni)
        cliente.append(nombre)
        cliente.append(apellidos)
        cliente.append(int(telefono))
        lista.append(np.array(cliente))
    elif len(lista)>0:#Cuando ya haya aunque sea un cliente en la lista de clientes, se hara la comprobacion que no exista antes de agregarlo
        repetido=False
        for i in lista:
            if np.any(i[0]==dni):#Comprobamos dentro de cada array, el dato que sería el DNI. Si existe, se pondra el boolean 'repetido' como True
                repetido=True
        if repetido==False:
            cliente.append(dni)
            cliente.append(nombre)
            cliente.append(apellidos)
            cliente.append(telefono)
            lista.append(np.array(cliente))
        elif repetido==True:
            print("El cliente ya se encuentra en la base de datos. No se agregara a la lista")

def formatoDNI(a):
    formato=False
    while formato==False:
        for i in a:
            if i.isalpha():
                formato=True
        if formato==False:
            a=input("El DNI debe tener una vocal")
    return a


def listarClientes(lista):#Funcion para listar los cliente
    if len(lista)==0:#Si la lista está vacía avisará
        print("No hay clientes en la base de datos.")
    elif len(lista)>0:#Si la lista tiene clientes, los mostrará
        for i in lista:
            print(i)
def buscarDNI(lista,funcion):#Funcion para buscar en la lista por dni
    if funcion==0:
        dni=input("Escribe el DNI a buscar\n")
    elif funcion==1:
        dni=input("Escribe el DNI del cliente que queremos cambiar su télefono\n")
    elif funcion==2:
        dni=input("Escribe el DNI del cliente que queremos eliminar\n")
    dni=dni.upper()
    encontrado=False
    for i in lista:
        if np.any(i[0]==dni):
            if funcion==0:
                print(tabulate(i, headers=["DNI","Nombre","Apellidos","Télefono"], tablefmt="fancy_grid"))
                encontrado=True
            elif funcion==1:
                encontrado=True
                return i, encontrado
            elif funcion==2:
                encontrado=True
                return i, encontrado

    if encontrado==False:
        print("Cliente no encontrado")

def modificarTelefono(lista):#Funcion para modificar lista 
    funcion=1
    cliente, encontrado=buscarDNI(lista, funcion)#Usamos la funcion buscar DNI para no repetir el codigo 
    if encontrado==True:#Solo si encuentra el DNI pediremos el telefono
        telefono=input("Escribe el nuevo número de telefono")
        telefono=esNumerico(telefono)
        for i in lista:
            if np.any(i[0]==cliente[0]):#Cuando el DNI del cliente coincida en la lista, se modificará el valor telefono
                i[3]==telefono
                print("Télefono modificado correctamente")
    

def eliminarCliente(lista):#Funcion para eliminar clientes
    funcion=2
    cliente,encontrado=buscarDNI(lista,funcion)#Usamos la funcion buscar DNI para no repetir el codigo
    if encontrado==True:#Solo si encuentra el DNI recorreremos la lista para eliminar el cliente
        for i in lista:
            if np.any(cliente[0]==i[0]):
                lista.pop(i)
                print("Cliente eliminado correctamente")


def guardarListaClientes(lista,ruta):#Funcion para guardar los datos de los clientes. Usaremos una ruta(Path) ya definida 
    if len(lista)==0:
        print("No hay clientes que guardar.")
    elif len(lista)>0:
        modo='ab' if  ruta.exists() else 'wb' #ruta.exists() comprueba que un archivo Path exista donde se indica, devolviendo True/False.
        with open(ruta, modo) as archivo:
            pkl.dump(lista, archivo)
        print("Clientes guardados")

def cargarLista(ruta):#Funcion para cargar los datos de los clientes en la lista. 
    if not ruta.exists():
        print("No hay archivos guardados")
    else:
        datos=[]
        continuar=True
        with open(ruta, 'rb') as archivo:
            while continuar==True:#Condicion para continuar leyendo
                try:
                    dato=pkl.load(archivo)
                    datos.append(dato)
                except EOFError:#Error E0FError es error de fin del archivo. 
                    continuar=False
        lista=[]
        for dato in datos:
            lista.append(np.array(dato))
        print("Datos cargados")
        return lista


def esNumerico(a):#Funcion para comprobar que sea númerico
    while a.isalpha():
        a=input("El valor debe ser númerico.")
    a=int(a)
    return a