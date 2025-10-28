import funciones_tienda

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
                funciones_tienda.añadirADicc(articulo,a,valor)   
                n+=1
            case 1:
                a="Nombre"
                valor=input(f"Escribe el {a} del articulo\n")
                funciones_tienda.añadirADicc(articulo,a,valor)
                n+=1

            case 2:
                a="Precio"
                valor=input(f"Escribe el {a} del articulo\n")
                valor=float(funciones_tienda.esNumerico(valor))
                funciones_tienda.añadirADicc(articulo,a,valor)
                n+=1
                
            case 3:
                a="Stock"
                valor=input(f"Escribe el {a} del articulo\n")
                valor=funciones_tienda.esNumerico(valor)
                valor=int(valor)
                funciones_tienda.añadirADicc(articulo,a,valor)
                n+=1
            case 4:
                a="Activo"
                valor=funciones_tienda.disponibilidad()
                funciones_tienda.añadirADicc(articulo,a,valor)
                n+=1
            
    return articulo


def modArticulo(a,b,i,n):
    b=input(f"Escribe el nuevo {a}\n")
    if a=="Precio":
        b=float(b)
    elif a=="Stock":
        b=int(b)
    i[a]=b  
    n=1
    return n