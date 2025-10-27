def confirmarCompra(carro,user,reg,lista):#Funcion donde se confirmara la compra.
    valorTotal=0
    for i in carro:
        valorTotal+=i["Precio"]*i["Cantidad"]
        print(i)
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
        reg[n]=(user,venta)#Se le asigna al carrito un numero unico de venta y una tupla que contenga el usuario y la lista de disccionarios de la compra.
    else:
        print("Se cancelo la compra.")

def restaStock(lista,carro):
    for i in lista:
        for j in carro:
            if i["ID"]==j["ID"]:
                i["Stock"]-=j["Cantidad"]

def vaciar(carro):
    x=input("Se va a vaciar el carrito. Escribe 1 para confirmar vaciar el carrito, 0 para cancelar.")
    if x==1:
        carro.clear()