#importamos librerias
import damas_core

#Definimos funciones
def movimientosJ1(tablero,x,y,movValido):
    if tablero[y,x]==1 or tablero[y,x]==2:
            if tablero[y,x]==1:
                while movValido==False:
                    mov=input("Puedes mover la ficha en diagonal hacia abajo. Presiona 0 para la izquierda, 1 para la derecha\n")
                    mov=damas_core.esNumerico(mov)
                    rangoVal=enRango(x,y,mov)
                    if mov==0 and rangoVal==True:
                        if tablero[y+1,x-1]==0:
                            tablero[y,x]=0
                            tablero[y+1,x-1]=1
                            x=x-1
                            y=x+1

                            #Aqui ira la comprobacion de comer

                    if mov==1 and rangoVal==True:
                        if tablero[y+1,x+1]==0:
                            tablero[y,x]=0
                            tablero[y+1,x+1]=1

                            #Aqui ira la comprobacion de comer


def enRango(x,y,mov):#Funcion que nos comprobará si se puede hacer el movimiento(si no se sale del tablero)
    rangoVal=False
    if mov==0:
        if x-1>=0:
            rangoVal=True
    if mov==1:
        if x+1<=7:
            rangoVal=True
    return rangoVal

def comprobacionPeon(x,y,tablero,mov):
    if mov==0:
        if x>=2:
            
        if x<2:

    if mov==1:
        if 