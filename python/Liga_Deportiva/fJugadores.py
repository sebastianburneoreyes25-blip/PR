#importamos libreiras
import fGenerales


#Funciones para menu jugadores

def fichaJugadores(lista,lista2):
    n=0
    datos={}
    while n!=6:
        n+=1
        match n:
            case 1:
                id=fGenerales.generaraId(lista)
                datos["ID"]=id
                print(f"Se ha generado un ID {id}")
            case 2:
                nom=input("Escribe el nombre del jugador\n")
                datos["Nombre"]=nom
            case 3:
                pos=input("Escribe la posicion del jugador\n")
                datos["Posicion"]=pos
            case 4:
                x=0
                flag=False
                while x!=1:
                    equip=input("Escribe el id del equipo\n")
                    equip=fGenerales.esNumerico(equip)
                    for i in lista2:
                        if i["ID"]==equip:
                            datos["id_equipo"]=equip
                            x=1
                            flag=True
                    if flag==False:
                        x=input(f"El ID {equip} no se ha encontrado. Presiona 1 para cancelar el alta, 0 para volver a introducir el ID del equipo.\n")
                        x=fGenerales.esNumerico(x)  
                        if x==1: 
                            print("Operacion cancelada")             
            case 5:
                f=input("Equipo activo:1\nEquipo inactivo:0\n")
                f=fGenerales.activoIncativo(f)
                datos["Activo"]=f
                if flag==True:
                    lista.append(datos)

def mostrarJugadores(lista,lista2):
    op=input("Escribe 1 para mostrar todos, 2 para mostrar los de un equipo especifico\n")
    op=fGenerales.esNumerico(op)
    match op:
        case 1:
            fGenerales.mostrarListaDic(lista)
        case 2:
            equip=input("Escribe el id del equipo\n")
            equip=fGenerales.esNumerico(equip)
            jug=[]
            for i in lista2:
                if i["ID"]==equip:
                    for j in lista:
                        if i["ID"]==j["id_equipo"]:
                            jug.append(j)
            fGenerales.mostrarListaDic(jug)
