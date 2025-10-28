import funciones_tienda

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
                funciones_tienda.añadirADicc(user,a,valor)   
                n+=1
            case 1:
                a="Nombre"
                valor=input(f"Escribe el {a} del usuario\n")
                funciones_tienda.añadirADicc(user,a,valor)
                n+=1
            case 2:
                a="Email"
                valor=verificarMail()
                funciones_tienda.añadirADicc(user,a,valor)
                n+=1
            case 3:
                a="Activo"
                valor=funciones_tienda.disponibilidad()
                funciones_tienda.añadirADicc(user,a,valor)
                n+=1
    return user  

def verificarMail():#Funcion para verificar que el formato del mail es valido
    flag=True
    while flag==True:
                    valor=input(f"Escribe el email del usuario\n")
                    if "@" in valor and "." in valor:
                        flag=False
                    else:
                        print(f"El email {valor} no contiente \"@\" ni \".\", vuelve a escribirlo en un formato valido.")
    return valor

def modCliente(a,b,i,n):
    if a=="Email":
        b=verificarMail()
    else:
        b=input(f"Escribe el nuevo {a}\n")
    i[a]=b
    n=1
    return n