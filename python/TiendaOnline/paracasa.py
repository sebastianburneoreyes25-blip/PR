def confirmarCompra(carro,user,reg):
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
        venta=carrito.copy()
        carro.clear()
        reg[n]=(user,venta)
    else:
        print("Se cancelo la compra.")