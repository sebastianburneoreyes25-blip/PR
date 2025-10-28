import funciones_tienda

def mostrar_carro_historial(e,lista,flag):
    if int(e)==4:#Para mostrar el carrito
            for i in lista:
                funciones_tienda.imprimirLista(i)
    elif int(e)==6:#Para mostrar el registro de las ventas por id
        idbuscar=input("Selecciona el id a consultar")
        idbuscar=funciones_tienda.idNumerico(idbuscar)
        for a,(b,c,d) in lista.items():
            for k in b:  
                    #for k in c:    
                if idbuscar==k["ID"]:
                    print(c)
                    flag=True
            if flag==False:
                print("Id no encontrado.")

def vaciar(carro):
    x=input("Se va a vaciar el carrito. Escribe 1 para confirmar vaciar el carrito, 0 para cancelar.")
    if x=="1":
        carro.clear()

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


def select(lista1,lista,n):#Funcion para la seleccion del usuario(Usuario activo, añadir producto y cantidad)
    id=""
    id=input("Escribe el ID a seleccionar\n")
    id=funciones_tienda.idNumerico(id)
    diccionario={}
    flag=True
    x=0
    for i in lista:
        if n=="1":#Aqui se usara la variable para seleccionar el usuario
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
                if len(lista1)>0:#Cuando la lista este con algun articulo hara esta funcion
                    diccionario=añadir2(id,lista1,x,flag,diccionario,i).copy()
                    flag=False
                if len(lista1)==0:  #Cuando la lista este vacia hará esta funcion
                    diccionario=añadir1(i,x,flag,diccionario)   
                    flag=False
            elif i["ID"] ==id and i["Activo"]==False:
                print("La cuenta del usuario elegido esta desactivada, pruebe con otro o cambie el estado de la cuenta.")
                flag=False
    if flag==True:
        print("El ID no se encuentra en la base de datos,pruebe de nuevo o se han seleccionado más de los existentes.")
    
    return diccionario

def añadir2(id,lista1,x,flag,diccionario,i):
    for j in lista1:
        if id==j["ID"]:
            if x<=i["Stock"]:#Condicion de no dejar agregar al carrito más de los articulos que hay.
                c=j["Cantidad"]+x
                if c<=i["Stock"]:
                    j["Cantidad"]=int(c)
                    flag=False
            if x>i["Stock"] or (j["Cantidad"]+x)>i["Stock"]:
                print("Cantidad mayor a la disponible.")
                flag=False
        if id!=j["ID"]:
            diccionario,flag=añadir1(i,x,flag,diccionario)
    return diccionario

def añadir1(i,x,flag,diccionario):
    if x<=i["Stock"]:
        diccionario=articuloCarrito(diccionario,x,i)
        
    if x>i["Stock"] :
        print("Cantidad mayor a la disponible.")
        
    return diccionario


def articuloCarrito(diccionario,x,i):#Funcion para añadir nuevo articulo al carrito.
    diccionario=i.copy()
    diccionario["Cantidad"]=x
    diccionario.pop("Stock")
    diccionario.pop("Activo")
    return diccionario  