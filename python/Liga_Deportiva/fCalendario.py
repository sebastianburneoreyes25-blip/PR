import fGenerales
import datetime


#Definimos funciones
def fichaPartido(lista,lista2):
    n=0
    datos={}
    while n<8:
        n+=1
        if cancelar==True:
            n=9
        match n:
            case 1:
                id=fGenerales.generaraId(lista)
                datos["ID"]=id
                print(f"Se ha generado un ID {id}")
            case 2:
                jor=input("Escribe la jornada en la que se jugará\n")
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
                                       if a!=1:
                                            print("Operacion cancelada")
                                            cancelar=True
                                            x=1                                                
                    if flag==False:
                        x=input(f"El ID {visit} no se ha encontrado. Presiona 1 para cancelar el alta, 0 para volver a introducir el ID del equipo.\n")
                        x=fGenerales.esNumerico(x)  
                        if x==1: 
                            print("Operacion cancelada")             
            case 5:
                f=input("¿En que fecha se jugará el partido? (año/mes/dia)\n")
                f=comprobarFecha(f)
                datos["Fecha"]=f
                if flag==True:
                    lista.append(datos)


def comprobarFecha(a):
    x=True
    while x==True:
        try:
            datetime.strptime(a,'%Y-%m-%d')
            print("Fecha valida")
            x=False
            return  a
        except:
            print("Fecha invalida")


