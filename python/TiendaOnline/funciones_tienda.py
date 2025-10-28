#Importamos librerias
import funciones_articulos
import funciones_clientes
import funciones_ventas

#Definimos funciones

def menu(lista):
    for i in lista:
        print(f"{i}")

def añadirADicc(cosa,a,b): #Añade un valor al dicc, se podra usar tanto para los usuarios como para los articulos.
    cosa[a]=b

def crear(cosa,lista,tipo): #Funcion para agregar un diccionario a la lista correspondiente
    if tipo=="1":
        cosa=funciones_articulos.fichaArticulo(cosa,lista)
    elif tipo=="2":
        cosa=funciones_clientes.fichaUser(cosa,lista)
    lista.append(cosa)


def esNumerico(valor):#Nos aseguramos que sea numerico la variable dada
    while valor.isalpha():
        valor=input("El dato añadido debe de ser numerico.")
    return valor
                
def disponibilidad():#Asignaremos un boolean para determinar si esta activo o inactivo sin borrar el articulo del sistema
    disp=2
    status=""
    while disp!=0 and disp!=1:
        disp=int(input("Escribe 0 para estado inactivo, 1 para estado activo\n"))
        match disp:
            case 0:
                status=False
            case 1:
                status=True
            case _:
                print("Comando no disponible, intentalo de nuevo")
    
    return status


def mostrarLista(lista,n,e): #Funcion para mostrar el inventario
    flag=False
    if int(n)<3:
        s=int(input("Escribe 1 para mostrar solo activos, 0 para los inactivos.\n")) #Se usara el numero usado para buscar True or False
        m=""
        if s==1:
            m=True
        elif s==0:
            m=False
        else:
            print("Comando no valido, vuelve a probar")
        for i in lista:
            if i["Activo"]==m:#Solo hara el print de los articulos True or False
                imprimirLista(i)
    elif int(n)==3 :
        funciones_ventas.mostrar_carro_historial(e,lista,flag)
                       
def imprimirLista(i):#
    valor=""
    for a,b in i.items():
        listar=f"{a} : {b}  "
        valor+=listar
    print(valor)

def buscarPorId(lista): #Busca articulos por ID
    flag=False
    n=0
    idBuscar=input("Escribe el id a buscar.\n")
    if not idBuscar.isalpha():
        idBuscar=int(idBuscar)
        valor=""
        for i in lista:
            flag=False
            for a,b in i.items():
                if i["ID"]==idBuscar:
                    flag=True
                    listar=f"{a} : {b}  "
                    valor+=listar
            if flag==True:
                print(valor)
                n=1
        if flag==False and n==0:
            print(f"El producto con id {idBuscar} no ha sido encontrado. Pruebe de nuevo") 
    else:
        print(f"El id {idBuscar} debe ser un numero")



def actualizar(lista,tipo): #Funcion para actualizar
    flag=False
    n=0
    if tipo=="1":
        print("Los parametros que se pueden actualizar son:\n-Nombre\n-Precio\n-Stock")
    if tipo=="2":
        print("Los parametros que se pueden actualizar son:\n-Nombre\n-Email\n")
    idBuscar=input("Escribe el id a actualizar.\n") #Busca  por ID
    idBuscar=idNumerico(idBuscar)
    flag=False
    for i in lista:
        flag=False
        if n!=1 and i["ID"]==idBuscar:
            param=input("Escribe el parametro a actualizar.\n")  
            paraml=param.lower() #Convierto el parametro puesto a minusculas para comparar
            if paraml=="id":
                print("No se puede cambiar el ID.")
            else:
                for a,b in i.items():
                    al=a.lower()
                    if i["ID"]==idBuscar:
                        flag=True
                        if al==paraml:
                            if tipo=="1":
                                n=funciones_articulos.modArticulo(a,b,i,n)
                            elif tipo=="2":
                                n=funciones_clientes.modCliente(a,b,i,n)
    if flag==False and n==0:
        print(f"El producto con id {idBuscar} no ha sido encontrado. Pruebe de nuevo") 



def eliminar(lista): #Funcion para borrar articulos por ID
    flag=True
    idBuscar=input("Escribe el id a eliminar.\n")
    idBuscar=idNumerico(idBuscar)
    for i in lista:
        if i["ID"]==idBuscar:
            conf=input("Escribe 1 para confirmar la eliminacion, 2 para cancelar\n")
            if conf=="1":
                lista.remove(i)
                flag=False
    if flag==True:
        print(f"El producto con id {idBuscar} no ha sido encontrado. Pruebe de nuevo")
    if flag==False:
        print(f"El producto con id {idBuscar} se ha eliminado.")  
    
def alernarStatus(lista):
    idBuscar=input("Escribe el id a cambiar su estado.\n")
    idBuscar=idNumerico(idBuscar)
    flag=False
    for i in lista:
        if i["ID"]==idBuscar:
            i["Activo"]=disponibilidad()
            flag=True
    if flag==False:
        print("Id no encontrado, pruebe de nuevo.\n")

def idNumerico(idBuscar):#Como se necesita en varios sitios de la misma manera creo funcion para comprobar que el id sea numerico y no letras.Despues se transforma a int para que se consiga leer bien.
    while idBuscar.isalpha():
        idBuscar=input("El ID debe ser numerico, escribelo de nuevo\n")
    idBuscar=int(idBuscar)

    return idBuscar


