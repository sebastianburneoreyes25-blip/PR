#Definimos variables
producto={
}
listaArticulos=[
]
user={
}
listaUsuarios=[
]
carrito=[
]
registroVentas={
}
usuarioActivo=[
]
eleccion=""
tipo=""
n=False

#Definimos funciones

def menuArticulos():  #Funcion para mostrar el menu de opciones de los articulos
    print("1.Crear articulo\n2.Listar articulos\n3.Buscar articulo por id.\n4.Actualizar articulo\n5.Eliminar articulo\n6.Alternar activo/inactivo\n7.Salir\n")

def menuUsuarios():  #Funcion para mostrar el menu de opciones de los usuario
    print("1.Crear usuario\n2.Listar usuario\n3.Buscar usuario por id.\n4.Actualizar usuario\n5.Eliminar usuario\n6.Alternar activo/inactivo\n7.Salir\n")

def menuOpciones():#Función que nos permitira ir al menu de usuarios, de productos o salir de la app.
    print("Elige el menu:\n-1.Articulos\n-2.Usuario\n-3.Ventas/Carrito\n-4.Salir\n")

def menuVentas():#Funcion que nos permitira ver el menu de las opciones para las ventas y carrito
    print("VENTAS / CARRITO\n\n1.Seleccionar usuario activo\n2.Añadir articulo al carrito\n3.Quitar articulos del carrito\n4.Ver carito (detalles y total)\n5.Confirmar compra\n6.Historial de ventas por usuario\n7.Vaciar carrito\n8.Salir")

def añadirADicc(cosa,a,b): #Añade un valor al dicc, se podra usar tanto para los usuarios como para los articulos.
    cosa[a]=b

def crear(cosa,lista,tipo): #Funcion para agregar un diccionario a la lista correspondiente
    if tipo=="1":
        cosa=fichaArticulo(cosa,lista)
    elif tipo=="2":
        cosa=fichaUser(cosa,lista)
    lista.append(cosa)

def fichaArticulo(articulo,lista): #Con un bucle while y un match case el usuario ira rellenando la ficha del articulo ESTO ES SOLO FICHA, para crear se usa la funcion crearArticulo
    articulo={}              #Definimos el articulo como un diccionario vacio para rellenar
    n=0
    m=0
    while n!=5:
        flag=True
        match n:
            case 0:
                a="ID"
                m+=len(lista)+1
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
                valor=input(f"Escribe el {a} del articulo\n")
                valor=float(esNumerico(valor))
                añadirADicc(articulo,a,valor)
                n+=1
                
            case 3:
                a="Stock"
                valor=input(f"Escribe el {a} del articulo\n")
                valor=esNumerico(valor)
                valor=int(valor)
                añadirADicc(articulo,a,valor)
                n+=1
            case 4:
                a="Activo"
                valor=disponibilidad()
                añadirADicc(articulo,a,valor)
                n+=1
            
    return articulo

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
        if int(e)==4:#Para mostrar el carrito
            for i in lista:
                imprimirLista(i)
        elif int(e)==6:#Para mostrar el registro de las ventas por id
            for a,(b,c,d) in lista.items():
                idbuscar=input("Selecciona el id a consultar")
                idbuscar=idNumerico(idbuscar)
                for k in c:    
                    if idbuscar==k["ID"]:
                        print(c)
                        flag=True
            if flag==False:
                print("Id no encontrado.")
                       
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
                                b=input(f"Escribe el nuevo {a}\n")
                                if a=="Precio":
                                    b=float(b)
                                i[a]=b
                                n=1
                            elif tipo=="2":
                                if a=="Email":
                                    b=verificarMail()
                                else:
                                    b=input(f"Escribe el nuevo {a}\n")
                                i[a]=b
                                n=1
    if flag==False and n==0:
        print(f"El producto con id {idBuscar} no ha sido encontrado. Pruebe de nuevo") 

def verificarMail():#Funcion para verificar que el formato del mail es valido
    flag=True
    while flag==True:
                    valor=input(f"Escribe el email del usuario\n")
                    if "@" in valor and "." in valor:
                        flag=False
                    else:
                        print(f"El email {valor} no contiente \"@\" ni \".\", vuelve a escribirlo en un formato valido.")
    return valor

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
    n=0
    idBuscar=input("Escribe el id a cambiar su estado.\n")
    idBuscar=idNumerico(idBuscar)
    flag=False
    for i in lista:
        if i["ID"]==idBuscar:
            i["Activo"]=disponibilidad()
            flag=True
    if flag==False:
        print("Id no encontrado, pruebe de nuevo.\n")


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

def userSelect(lista1,lista,n):#Funcion para la seleccion del usuario(Usuario activo, añadir producto y cantidad)
    id=""
    id=input("Escribe el ID a seleccionar\n")
    id=idNumerico(id)
    diccionario={}
    flag=True
    x=0
    for i in lista:
        if n=="1":#Aqui se usara lavariable apra seleccionar el ususario
            if i["ID"] ==id and i["Activo"]==True:
                lista1.clear()
                diccionario=i.copy()
                flag=False
            elif i["ID"] ==id and i["Activo"]==False:
                print("La cuenta del usuario elegido esta desactivada, pruebe con otro o cambie el estado de la cuenta.")
                flag=False
        elif n=="2":#Esta será la variable que nos permita seleccionar el item para el carrito
            if i["ID"] ==id and i["Activo"]==True:
                x=input("¿Cuantos articulos vas a agregar?\n")
                while x.isalpha():
                    x=input("La cantidad debe ser numeros enteros.Prueba de nuevo\n")
                x=int(x)
                if len(lista1)>0:
                    for j in lista1:
                        if j["ID"] in lista1:
                            if x<i["Stock"] and (j["Cantidad"]+x)<i["Stock"]:#Condicion de no dejar agregar al carrito más de los articulos que hay.
                                c=j["Cantidad"]
                                j["Cantidad"]=int(c)+x
                                flag=False
                            if x>i["Stock"] or (j["Cantidad"]+x)>i["Stock"]:
                                print("Cantidad mayor a la disponible.")
                        if j["ID"] not in lista1:
                            if x<i["Stock"]:
                                diccionario=articuloCarrito(diccionario,x,i)
                                flag=False
                            if x>i["Stock"]:
                                print("Cantidad mayor a la disponible.")
                if len(lista1)==0:
                        if x<i["Stock"]:
                            diccionario=articuloCarrito(diccionario,x,i)
                        if x>i["Stock"] :
                            print("Cantidad mayor a la disponible.")
                flag=False
            elif i["ID"] ==id and i["Activo"]==False:
                print("La cuenta del usuario elegido esta desactivada, pruebe con otro o cambie el estado de la cuenta.")
                flag=False
    if flag==True:
        print("El ID no se encuentra en la base de datos,pruebe de nuevo o se han seleccionado más de los existentes.")
    
    return diccionario

def articuloCarrito(diccionario,x,i):#Funcion para añadir nuevo articulo al carrito.
    diccionario=i.copy()
    diccionario["Cantidad"]=x
    diccionario.pop("Stock")
    diccionario.pop("Activo")
    return diccionario    

def idNumerico(idBuscar):#Como se necesita en varios sitios de la misma manera creo funcion para comprobar que el id sea numerico y no letras.Despues se transforma a int para que se consiga leer bien.
    while idBuscar.isalpha():
        idBuscar=input("El ID debe ser numerico, escribelo de nuevo\n")
    idBuscar=int(idBuscar)

    return idBuscar

def confirmarCompra(carro,user,reg,lista):#Funcion donde se confirmara la compra.
    valorTotal=0
    for i in carro:
        valorTotal+=i["Precio"]*i["Cantidad"]
        print(f"-{i["Nombre"]} {i["Precio"]}€ {i["Cantidad"]} Uds" )
    print(f"El precio total a pagar sera {valorTotal}€.")
    x=input("1 para confirmar, 0 para cancelar\n")
    while x.isalpha():
        x=input("Se necesta un valor númerico.\n")
    x=int(x)
    n=len(reg)+1
    venta=[]
    if x==1:
        venta=carro.copy()#Copiamos el carro en venta
        restaStock(lista,carro)#Restamos el stock
        carro.clear()#Como se coonfirma la compra, se vacia el carrito
        reg[n]=(user,venta,f"{valorTotal}€")#Se le asigna al carrito un numero unico de venta y una tupla que contenga el usuario y la lista de disccionarios de la compra.
    else:
        print("Se cancelo la compra.")

def restaStock(lista,carro):#Funcion para restar al stock la cantidad de productos seleccionados
    for i in lista:
        for j in carro:
            if i["ID"]==j["ID"]:
                i["Stock"]-=j["Cantidad"]

def vaciar(carro):
    x=input("Se va a vaciar el carrito. Escribe 1 para confirmar vaciar el carrito, 0 para cancelar.")
    if x=="1":
        carro.clear()

#Logica de programacion
while tipo!="4":
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
                        mostrarLista(listaArticulos,tipo,eleccion)
                    case "3":
                        buscarPorId(listaArticulos)
                    case "4":
                        actualizar(listaArticulos,tipo)####Nota para mi: modificar para no poder cambiar id nunca
                    case "5":
                        eliminar(listaArticulos)
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
                        mostrarLista(listaUsuarios,tipo,eleccion)
                    case "3":
                        buscarPorId(listaUsuarios)
                    case "4":
                        actualizar(listaUsuarios,tipo)
                    case "5":
                        eliminar(listaUsuarios)
                    case "6":
                        alernarStatus(listaUsuarios)
                    case "7":
                        print("Sayonara baby!!")
                    case _:
                        print("No entendi el comando. Prueba de nuevo")
        case "3":
            while eleccion!="8":
                menuVentas()
                eleccion=input("Elige una operacion.\n")
                match eleccion:
                    case "1":
                        usuarioActivo.append(userSelect(usuarioActivo,listaUsuarios,eleccion))
                        if len(usuarioActivo)>0:
                            n=True
                        else:
                            n=False
                    case "2":
                        if n==True:
                            producto=userSelect(carrito, listaArticulos,eleccion)
                            carrito.append(producto)
                        if n==False:
                            print("Se necesita tener un usuario seleccionado para agregar productos.")
                    case "3":
                        if len(carrito)>0:
                            eliminar(carrito)
                        else:
                            print("No hay articulos para eliminar")
                    case "4":
                        mostrarLista(carrito,tipo,eleccion)
                    case "5":
                       confirmarCompra(carrito,usuarioActivo,registroVentas,listaArticulos)
                    case "6":
                        mostrarLista(registroVentas,tipo,eleccion)
                    case "7":
                        vaciar(carrito)
                    case "8":
                        print("Sayonara baby!")
                    case _:
                        print("No entendi el comando. Prueba de nuevo")
        case "4":
            print("Hasta la vista ganster")
        case _:
            print("No entendi el comando, prueba de nuevo")