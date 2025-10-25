#Definimos variables
producto={
}
listaArticulos=[
]
user={
}
listaUsuarios=[
]
eleccion=""
tipo=""



#Definimos funciones

def menuArticulos():  #Funcion para mostrar el menu de opciones de los articulos
    print("1.Crear articulo\n2.Listar articulos\n3.Buscar articulo por id.\n4.Actualizar articulo\n5.Eliminar articulo\n6.Alternar activo/inactivo\n7.Salir\n")

def menuUsuarios():  #Funcion para mostrar el menu de opciones de los usuario
    print("1.Crear usuario\n2.Listar usuario\n3.Buscar usuario por id.\n4.Actualizar usuario\n5.Eliminar usuario\n6.Alternar activo/inactivo\n7.Salir\n")

def menuOpciones():#Función que nos permitira ir al menu de usuarios, de productos o salir de la app.
    print("Elige el menu:\n-1.Articulos\n-2.Usuario\n-3.Salir\n")

def añadirADicc(cosa,a,b): #Añade un valor al dicc, se podra usar tanto para los usuarios como para los articulos.
    cosa[a]=b


def crear(cosa,lista,tipo): #Funcion para agregar un articulo a la lista de articulos
    if tipo=="1":
        cosa=fichaArticulo(cosa,lista)
    elif tipo=="2":
        cosa=fichaUser(cosa,lista)
    lista.append(cosa)


def fichaArticulo(articulo): #Con un bucle while y un match case el usuario ira rellenando la ficha del articulo ESTO ES SOLO FICHA, para crear se usa la funcion crearArticulo
    articulo={}              #Definimos el articulo como un diccionario vacio para rellenar
    n=0
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
                a="Activo"
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


def mostrarLista(lista): #Funcion para mostrar el inventario

    valor=""
    s=int(input("Escribe 1 para mostrar solo activos, 0 para los inactivos.\n")) #Se usara el numero usado para buscar True or False
    m=""
    if s==1:
        m=True
    elif s==0:
        m=False
    else:
        print("Comando no valido, vuelve a probar")
    for i in lista:
        valor=""
        if i["Activo"]==m:#Solo hara el print de los articulos True or False
            for a,b in i.items():
                    listar=f"{a} : {b}  "
                    valor+=listar
                    articulo=valor
            print(articulo)
            
  
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
    else:
        print(f"El id {idBuscar} debe ser un numero")



def actualizar(lista,tipo): #Funcion para actualizar
    flag=False
    n=0
    if tipo=="1":
        print("Los parametros que se pueden actualizar son:\n-ID\n-Nombre\n-Precio\n-Stock")
    if tipo=="2":
        print("Los parametros que se pueden actualizar son:\n-ID\n-Nombre\n-Precio\n-Stock")
    idBuscar=input("Escribe el id a actualizar.\n") #Busca  por ID
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
                    if tipo=="1":
                        b=input(f"Escribe el nuevo {a}\n")
                        if a=="Precio":
                            b=float(b)
                        i[a]=b
                        flag=True
                        n=1
                    elif tipo=="2":
                        if a=="Email":
                            b=verificarMail()
                        else:
                            b=input(f"Escribe el nuevo {a}\n")
                        i[a]=b
                        flag=True
                        n=1
    if flag==False and n==0:
        print(f"El producto con id {idBuscar} no ha sido encontrado. Pruebe de nuevo") 

def verificarMail():
    flag=True
    while flag==True:
                    valor=input(f"Escribe el email del usuario\n")
                    if "@" in valor and "." in valor:
                        flag=False
                    else:
                        print(f"El email {valor} no contiente \"@\" ni \".\", vuelve a escribirlo en un formato valido.")

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
    idBuscar=int(input("Escribe el id del articulo a cambiar su estado.\n"))
    for i in lista:
        if i["ID"]==idBuscar:
            i["Disponibilidad"]=disponibilidad()


def fichaUser(user,lista):#Funcion para rellenar los datos de la ficha del usuario
    n=0
    user={}
    m=len(lista)
    while n!=4:
        match n:
            case 0:
                a="ID"
                m+=1
                valor=m
                print(f"Se ha creado usuario con ID {valor}")
                añadirADicc(user,a,valor)   
                n+=1
            case 1:
                a="Nombre"
                valor=input(f"Escribe el {a} del usuario\n")
                añadirADicc(user,a,valor)
                n+=1
            case 2:
                a="Email"
                valor=verificarMail()
                añadirADicc(user,a,valor)
                n+=1
            case 3:
                a="Activo"
                valor=disponibilidad()
                añadirADicc(user,a,valor)
                n+=1
    return user

            
    

#Logica de programacion
while tipo!="3":
    tipo=""
    eleccion=""
    menuOpciones()
    tipo=str(input("Elige el tipo de operacion.\n"))
    match tipo:
        case "1":
            while eleccion!="7":
                menuArticulos()
                eleccion=input("Elige una operacion.\n")
                match eleccion:
                    case "1":
                        crear(producto,listaArticulos,tipo)
                    case "2":
                        mostrarLista(listaArticulos)
                    case "3":
                        buscarPorId(listaArticulos)
                    case "4":
                        actualizar(listaArticulos,tipo)
                    case "5":
                        eliminarArtic(listaArticulos)
                    case "6":
                        alernarStatus(listaArticulos)
                    case "7":
                        print("Sayonara baby!!")
                    case _:
                        print("No entendi el comando. Prueba de nuevo")
        case "2":
            while eleccion!="7":
                menuUsuarios()
                eleccion=input("Elige una operacion.\n")
                match eleccion:
                    case "1":
                        crear(user,listaUsuarios,tipo)
                    case "2":
                        mostrarLista(listaUsuarios)
                    case "3":
                        buscarPorId(listaUsuarios)
                    case "4":
                        actualizar(listaUsuarios,tipo)
                    case "5":
                        eliminarArtic(listaUsuarios)
                    case "6":
                        alernarStatus(listaUsuarios)
                    case "7":
                        print("Sayonara baby!!")
                    case _:
                        print("No entendi el comando. Prueba de nuevo")
        case "3":
            print("Hasta la vista ganster")
        case _:
            print("No entendi el comando, prueba de nuevo")