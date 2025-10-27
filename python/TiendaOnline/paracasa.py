def confirmarCompra(carro,user,reg,lista):
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
        venta=carro.copy()
        restaStock(lista,carro)
        carro.clear()
        reg[n]=(user,venta)
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