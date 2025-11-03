import fGenerales
from datetime import datetime
import tabulate


#Definimos funciones
def fichaPartido(lista,lista2):
    n=0
    datos={}
    cancelar=False
    while n<7:
        n+=1
        if cancelar==True:
            n=8
        match n:
            case 1:
                id=fGenerales.generaraId(lista)
                datos["ID"]=id
                print(f"Se ha generado un ID {id}")
            case 2:
                jor=input("Escribe la jornada en la que se jugará\n")
                jor=fGenerales.esNumerico(jor)
                while jor<1:
                    jor=input("La jornada no puede ser menor que 1\n")
                    jor=fGenerales.esNumerico(jor)
                datos["Jornada"]=jor
            case 3:
                x=0
                flag=False
                while x!=1:
                    local=input("Escribe el ID del equipo local\n")
                    local=fGenerales.esNumerico(local)
                    for i in lista2:
                        if local==i["ID"]:
                            datos["ID Local"]=local
                            x=1
                            flag=True
                    if flag==False:
                        x=input(f"El ID {local} no se ha encontrado. Presiona 1 para cancelar el alta, 0 para volver a introducir el ID del equipo.\n")
                        x=fGenerales.esNumerico(x)  
                        if x==1: 
                            print("Operacion cancelada")
                            cancelar=True 
            case 4:
                x=0
                flag=False
                while x!=1:
                    flag=False
                    visit=input("Escribe el id del equipo visitante\n")
                    visit=fGenerales.esNumerico(visit)
                    for i in lista2:
                        if i["ID"]==visit:
                                if visit!=datos["ID Local"]:
                                    datos["ID Visitante"]=visit
                                    x=1
                                    flag=True
                                if visit==datos["ID Local"]:
                                       a=input("El ID del visitante no puede ser igual al del local. Introduce 1 para volver a definir el ID, cualquier otro numero para cancelar el alta\n")
                                       a=fGenerales.esNumerico(a)
                                       flag=True
                                       if a!=1:
                                            print("Operacion cancelada")
                                            cancelar=True
                                            x=1
                    if flag==False:
                        x=input(f"El ID {visit} no se ha encontrado. Presiona 1 para cancelar el alta, 0 para volver a introducir el ID del equipo.\n")
                        x=fGenerales.esNumerico(x)  
                        if x==1: 
                            print("Operacion cancelada") 
                            cancelar=True            
            case 5:
                f=input("¿En que fecha se jugará el partido? (año:mes:dia:horas:min)\n")
                f=comprobarFecha(f)
                datos["Fecha"]=f
            case 6:
                datos["Jugado"]=False
            case 7:
                datos["Resultado"]=None
                lista.append(datos)   

def mostrarCalendario(lista):#Funcion para mostrar el calendario de partidos.
    op=input("Escribe 1 para mostrar todos, 2 para mostrar una jornada especifica\n")
    op=fGenerales.esNumerico(op)
    match op:
        case 1:
            activos=[]
            for i in lista:
                    activos.append(i)
            print(tabulate.tabulate(activos, headers="keys", tablefmt="double_outline"))
        case 2:
            jor=input("Escribe el id de la jornada\n")
            jor=fGenerales.esNumerico(jor)
            part=[]
            for i in lista:
                if i["Jornada"]==jor:
                    part.append(i)
            fGenerales.desplegarDic(part)

def comprobarFecha(a):#Funcion para comprobar el formato de la fecha, que sea valido.
    a=datetime.strptime(a, "%Y:%m:%d:%H:%M")
    return  a

def repPartido(lista):#Funcion para modificar partido
    mostrarCalendario(lista)
    selec=input("Selecciona el id  a reprogramar")
    selec=fGenerales.esNumerico(selec)
    flag=False
    for i in lista:
        if i["ID"]==selec and i["Jugado"]==False:
            f=input("¿En que fecha se jugará el partido? (año:mes:dia:horas:min)\n")
            f=comprobarFecha(f)
            i["Fecha"]=f
        elif i["Jugado"]==True:
            print("No se puede reprogramar un partido ya jugado.")


def eliminarPartido(lista):#Funcion para eliminar por ID el partido
    mostrarCalendario(lista)
    selec=input("Selecciona el id a eliminar")
    selec=fGenerales.esNumerico(selec)
    flag=False
    for i in lista:
        if i["ID"]==selec and i["Jugado"]==False:
            lista.remove(i)
            print(f"El partido con id {selec} ha sido eliminado")
        elif i["Jugado"]==True:
            print("No se puede eliminar un partido ya jugado.")


