#Import 
import pickle

#Definimos variables
listaPalomas=[]
distancia=150
eleccion=0
menu=["1.Gestion de la carrera","2.Consultas","3.Guardar datos","4.Recuperar datos","5.Salir del programa"]
gestion=["a)Registrar Nueva Paloma","b)Registrar tiempo", "c)Regresar a menu."]
consultas=["a)Mostrar todas las palomas","b)Consulta a partir de la anilla","c)Mostrar palomas más rapidas", "d)Mostrar por propietario","e)Volver al menu"]
palomasDatos={}
sub=""

#Definimos funciones
def subeleccion(sub,lista):
    mostrarMenu(lista)
    sub=input("¿Que opción vas a realizar?\n")
    return sub


def esNumerico(a):
    while a.isalpha():
        a=input("El valor debe de ser numerico.Prueba de nuevo\n")
    a=int(a)
    return a

def mostrarMenu(lista):
    for a in lista:
        print(a)

def registrarPaloma(lista):
    anilla=input("Pon el codigo de la anilla\n")
    nombre=input("Dame el nombre de la paloma\n")
    propietario=input("¿Quien es su propietario?\n")
    propietario=propietario.upper()
    a=(anilla,nombre,propietario)
    lista.append(a)

def registratTiempo(listaPal,palomasDatos):
    pal=input("¿Que paloma vamos a comprobar? Escribe el codigo de la anilla.\n")
    pal_l=pal.lower()
    encontrada=False
    for palo in listaPal:
        for i in palo:
            il=i.lower()
            if il==pal_l:
                tiempo=input("¿Cuantos minutos a tardado en terminar el recorrido?\n")
                tiempo=esNumerico(tiempo)
                vMedia=distancia/(tiempo/60)
                vMedia=int(vMedia)
                a=[tiempo,vMedia]
                palomasDatos[pal]=a
                encontrada=True
    if encontrada==False:
        print("No se ha encontrado la paloma. Comprueba el codigo de la anilla y prueba de nuevo")

def mostrarPalomas(lista):
    for a,b,c in lista:
        print(f"Anilla:{a}  Nombre:{b}  Propietario.{c}\n")

def buscarPal(listapal,dicPal):
    datos=[]
    datosDic={}
    anilla=input("Introduce los datos de la anilla")
    encontrada=False
    carrera=False
    for pal in listapal:
        if anilla in pal:
            datos.append(pal)
            encontrada=True

        for a,b in dicPal.items():
            if anilla==a:
                datosDic[a]=b
                carrera=True
    
    if encontrada==True:
        if carrera==False:
            mostrarPalomas(datos)
        if carrera==True:
            mostrarPalomas(datos)
            for a,b in dicPal.items():
                i,j=b
                print(f"Tiempo total:{i}  Velocidad media: {j}")
    elif encontrada==False:
        print("No se ha encontrado la paloma. Comprueba que se ha introducido la anulla correctamente e intentalo de nuevo.")

def tierPalomas(dic):
    totalMedias=[]
    for a,b in dic.items():
        tiempo,vMedia=b
        totalMedias.append((a,vMedia))    
    top=sorted(totalMedias, key=lambda x:x[1], reverse=True)[:3]
    for a , b in top:
        print(f"Anilla:{a} Velocidad:{b}km/h")

def infoPropietario(lista):
    propietario=input("Escribe el nombre del propietario\n")
    propietario=propietario.upper()
    datos=[]
    for pal in lista:
        if propietario in pal:
            datos.append(pal)
    print(f"El propietario {propietario} tiene las siguientes palomas:")
    for pal in datos:
        print(pal)


def guardar(listaPalomas,dicPal):
    with open ('datos.pkl','wb') as archivo:
        pickle.dump(listaPalomas, archivo)
    with open('datosCarrera.pkl','wb') as archivodic:
        pickle.dump(dicPal,archivodic)
        

def cargar():
    with open ('datos.pkl', 'rb') as archivo:
        listaPalomas=pickle.load(archivo)
    return listaPalomas

#Logica de programación
while eleccion!=5:
    mostrarMenu(menu)
    eleccion=input("¿A que menu querras ir?\n")
    eleccion=esNumerico(eleccion)
    match eleccion:
        case 1:
            sub=subeleccion(sub,gestion)
            se_l=sub.lower()
            while se_l!="c":
                match se_l:
                    case "a":
                        registrarPaloma(listaPalomas)
                    case "b":
                        registratTiempo(listaPalomas,palomasDatos)
                    case "c":
                        print("Volviendo al menu")
                    case _:
                        print("No entendi el comando. Prueba de nuevo")
                sub=subeleccion(sub,gestion)
                se_l=sub.lower()
        case 2:
            sub=subeleccion(sub, consultas)
            se_l=sub.lower()
            while se_l!="e":
                match se_l:
                    case "a":
                        mostrarPalomas(listaPalomas)
                    case "b":
                        buscarPal(listaPalomas, palomasDatos)
                    case "c":
                        tierPalomas(palomasDatos)
                    case "d":
                        infoPropietario(listaPalomas)
                    case "e":
                        print("Volviendo al menu")
                    case _:
                        print("No entendí el comando")
                sub=subeleccion(sub, consultas)
                se_l=sub.lower()
        case 3:
            guardar(listaPalomas,palomasDatos)
        case 4:
            listaPalomas=cargar()
        case 5:
            print("Sayonara baby!!")
        case _:
            print("No entendí el comando")                    