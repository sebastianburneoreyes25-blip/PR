#Definimos variables
producto={

}

listaArticulos=[

]

inventario=""
eleccion=""

#Definimos funciones

def mostrarMenu():  #Funcion para mostrar el menu de opciones
    print("1.Crear articulo\n2.Listar articulos\n3.Buscar articulo por id.\n4.Actualizar articulo\n5.Eliminar articulo\n6.Alternar activo/inactivo\n7.Salir")

def añadirADicc(articulo,a,b): #Añade un valor al dicc
    articulo[a]=b

def crearArticulo(articulo,lista): #Funcion para agregar un articulo a la lista de articulos
    articulo=fichaArticulo(articulo)
    lista.append(articulo)


def fichaArticulo(articulo): #Con un bucle while y un match case el usuario ira rellenando la ficha del articulo ESTO ES SOLO FICHA, para crear se usa la funcion crearArticulo
    articulo={}              #Definimos el articulo como un diccionario vacio para rellenar
    n=0
    flag=True
    m=0
    while n!=5:
        flag=True
        match n:
            case 0:
                a="ID"
                m+=1
                valor=m
                print(f"Se ha creado articulo con ID {valor}")
                añadirADicc(articulo,a,valor)   
                n+=1
            case 1:
                a="Nombre"
                valor=input(f"Escribe el {a} del articulo\n")
                añadirADicc(articulo,a,valor)
                n+=1

            case 2:
                a="Precio"
                valor=float(input(f"Escribe el {a} del articulo\n"))
                añadirADicc(articulo,a,valor)
                n+=1
            case 3:
                a="Stock"
                valor=input(f"Escribe el {a} del articulo\n")
                añadirADicc(articulo,a,valor)
                n+=1
            case 4:
                a="Disponibilidad"
                valor=disponibilidad()
                añadirADicc(articulo,a,valor)
                n+=1
    return articulo
                
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



def mostrarArticulos(lista): #Funcion para mostrar el inventario
    valor=""
    s=int(input("Escribe 1 para mostrar solo activos, 0 para los incativos.\n")) #Se usara el numero usado para buscar True or False
    if s==1:
        m=True
    elif s==0:
        m=False
    else:
        print("Comando no valido, vuelve a probar")
    for i in lista:
        valor=""
        if i["Disponibilidad"]==m:#Solo hara el print de los articulos True or False
            for a,b in i.items():
                    listar=f"{a} : {b}  "
                    valor+=listar
                    articulo=valor
            print(articulo)
            
  
def buscarArticulo(lista): #Busca articulos por ID
    flag=False
    n=0
    idBuscar=input("Escribe el id a buscar.\n")
    valor=""
    for i in lista:
        flag=False
        for a,b in i.items():
            if b==idBuscar:
                flag=True
            elif flag==True:
                listar=f"{a} : {b}  "
                valor+=listar
        if flag==True:
            print(valor)
            n=1
    if flag==False and n==0:
        print(f"El producto con id {idBuscar} no ha sido encontrado. Pruebe de nuevo") 



def actualizar(lista): #Funcion para actualizar
    flag=False
    n=0
    idBuscar=input("Escribe el id del articulo a actualizar.\n") #Busca articulos por ID
    param=input("Escribe el parametro a actualizar.")  
    paraml=param.lower() #Convierto el parametro puesto a minusculas para comparar
    flag=False
    for i in lista:
        flag=False
        if n!=1:
            for a,b in i.items():
                al=a.lower()
                if idBuscar==b:
                    flag=True
                elif al==paraml:
                    b=input(f"Escribe el nuevo {a} ")
                    if a=="Precio":
                        b=float(b)
                    i[a]=b
                    flag=True
                    n=1
    if flag==False and n==0:
        print(f"El producto con id {idBuscar} no ha sido encontrado. Pruebe de nuevo") 

def eliminarArtic(lista): #Funcion para borrar articulos por ID
    flag=False
    n=0
    idBuscar=input("Escribe el id del articulo a eliminar.\n")
    for i in lista:
        flag=False
        if i["ID"]==idBuscar:
            flag=True
        if flag==True:
            conf=input("Escribe 1 para confirmar la eliminacion, 2 para cancelar\n")
            if conf=="1":
                lista.remove(i)
                flag=False
                n=1
    if flag==False and n==0:
        print(f"El producto con id {idBuscar} no ha sido encontrado. Pruebe de nuevo")
    if flag==False and n==1:
        print(f"El producto con id {idBuscar} se ha eliminado.")  
    
def alernarStatus(lista):
    n=0
    idBuscar=input("Escribe el id del articulo a cambiar su estado.\n")
    for i in lista:
        if i["ID"]==idBuscar:
            i["Disponibilidad"]=disponibilidad()

            


            
    

#Logica de programacion
mostrarMenu()
while eleccion!=7:
    eleccion=input("Elige una operacion.\n")
    match eleccion:
        case "1":
           crearArticulo(producto,listaArticulos)
        case "2":
            mostrarArticulos(listaArticulos)
        case "3":
            buscarArticulo(listaArticulos)
        case "4":
            actualizar(listaArticulos)
        case "5":
            eliminarArtic(listaArticulos)
        case "6":
            alernarStatus(listaArticulos)
        case "7":
            print("Sayonara baby!!")
        case _:
            print("No entendi el comando. Prueba de nuevo")
    mostrarMenu()