lista=[]
lista_l=[]
comidaFalta=""
com_l=comidaFalta.lower()
while com_l !="fin":
    comidaFalta=input("Escribe el nombre del producto a añadir\n")
    com_l=comidaFalta.lower()
    if com_l in lista_l and com_l!="fin":
        print("El articulo ya está en la lista.\n ")
    elif com_l=="fin":
        print("Se terminó de agregar árticulos.\nLista compra:")
        for a in lista:
            print(f"-{a}")
    else:
        lista.append(comidaFalta)
        lista_l.append(com_l)

