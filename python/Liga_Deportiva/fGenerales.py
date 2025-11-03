#Importamos librerias
import tabulate
import fGestion
import fJugadores

#Definimos variables

status=[True, False]


#Definimos funciones

def mostrarLista(lista):#Funcion para mostrar lista de listas.
    print(tabulate.tabulate(lista, headers=["Menu"], tablefmt="double_outline", stralign="left"))

def mostrarListaDic(lista):#Funcion para mostrar lista de diccionarios.
        activos=[]
        for i in lista:
            if i["Activo"]==True:
                activos.append(i)
        print(tabulate.tabulate(activos, headers="keys", tablefmt="double_outline"))

def bucarId(lista):#Funcion para mostrar el elemento que coincida con el id
    id=input("Escribe el id a buscar.")
    id=esNumerico(id)
    for i in lista:
        if i["ID"]==id:
            p=[]
            p.append(i)
    print(tabulate.tabulate(p, headers="keys"))

def posibilidadesUpdate(n):#Funcion para definir y mostrar los datos que se podran actualizar
    a=n.copy()
    a.pop("ID")
    a.pop("Activo")
    print("Se puede actualizar:")
    for x,y in a.items():
        print(f"-{x}")
    
    return a

def eliminarId(lista,lista2,e):#Funcion para eliminar por ID 
    mostrarListaDic(lista)
    selec=input("Selecciona el id a eliminar")
    selec=esNumerico(selec)
    flag=False
    for i in lista:
        if i["ID"]==selec:
            if e==1:
                for j in lista2:
                        if j["id_equipo"]==i["ID"]:
                            if i["Activo"]==True:
                                print("El equipo tiene jugadores asociados. No se puede eliminar")
                        elif j["id_equipo"]!=i["ID"]:
                            i["Activo"]=False
            elif  e==2:
                i["Activo"]=False
            elif e==3:
                if i["Jugado"]==False:
                    lista.remove(i)
                if i["Jugado"]==True:
                    print("No se puede eliminar un partido jugado")
       
def generaraId(lista):#Funcion que generara un ID en dependencia de la longitud de la lista
    id=0
    if len(lista)==0:
        id=1
    else:
        for i in lista:#Recorremos lista para ver el ultimo valor de id y asignarlo a la variable
            id=i["ID"]
        id+=1

    return id

    
def modificar(lista):
    mostrarListaDic(lista)
    selec=input("Selecciona el id  a modificar")
    selec=esNumerico(selec)
    flag=False
    for i in lista:
        if i["ID"]==selec:
            n=posibilidadesUpdate(i).copy()
            x=input("Selecciona una opcion a actualizar")
            xl=x.lower()
            for a,b in n.items():
                al=a.lower()
                if al==xl:
                    i[a]=input("Pon su nuevo dato")
                    flag=True
            if flag==False:
                print("Dato no encontrado. No se actualizara nada, prueba de nuevo.")

def esNumerico(n):
    while n.isalpha():
        n=input("El valor debe ser numerico")
    n=int(n)
    return n

def activoIncativo(f):
    f=esNumerico(f)
    while f not in status:
        f=input("La opciones son 1 o 0. Elige de nuevo\n")
        f=esNumerico(f)
    #if f==1:
    #    f=True
    #elif f==0:
    #     f=False
    f=f==1 #Funciona como lo de arriba
    return f


