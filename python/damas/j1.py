#importamos librerias
import damas_core

#Definimos funciones
def movimientosJ1(tablero,x,y,movValido,tablerouser):
    if tablero[y,x]==1 or tablero[y,x]==2:
        if tablero[y,x]==1:
            while movValido==False:
                mov=input("Puedes mover la ficha en diagonal hacia abajo. Presiona 0 para la izquierda, 1 para la derecha\n")
                mov=damas_core.esNumerico(mov)
                rangoVal=rangoPeon(x,y,mov)
                if mov==0 and rangoVal==True:
                    if tablero[y+1,x-1]==0:
                        tablero[y,x]=0
                        tablero[y+1,x-1]=1
                        tablerouser[y,x]='  '
                        tablerouser[y+1,x-1]="⚪"
                        x=x-1
                        y=x+1
                        comprobacionPeon(x,y,tablero,tablerouser)
                        movValido=True

                elif mov==1 and rangoVal==True:
                    if tablero[y+1,x+1]==0:
                        tablero[y,x]=0
                        tablero[y+1,x+1]=1
                        tablerouser[y,x]='  '
                        tablerouser[y+1,x+1]="⚪"
                        x=x+1
                        y=x+1
                        comprobacionPeon(x,y,tablero,tablerouser)
                        movValido=True

        if tablero[y,x]==2:
            while movValido==False:
                mov=input("Puedes mover la ficha en diagonal hacia abajo. Presiona 0 para la izquierda, 1 para la derecha\n")
                mov=damas_core.esNumerico(mov)
                cantidad=damas_core.esNumerico(input("¿Que cantidad de casillas quieres moverte?"))



def rangoPeon(x,y,mov):#Funcion que nos comprobará si se puede hacer el movimiento(si no se sale del tablero)
    rangoVal=False
    if mov==0:
        if x-1>=0 and y+1<=7:
            rangoVal=True
    if mov==1 and y+1<=7:
        if x+1<=7:
            rangoVal=True
    return rangoVal

def comprobacionPeon(x,y,tablero,tablerouser):#Hará la comprobación de que el peon como automaticamente si tiene una ficha en sus diagonales y un espacio vacio donde moverse.
    flag=False
    while flag==False:
        if x>=2 and y+2<=7:
            if tablero[y+1,x-1]>2 and tablero[y+2,x-2]==0:
                tablero[y,x]=0
                tablero[y+1,x-1]=0
                tablero[y+2,x-2]=1
                tablerouser[y,x]='  '
                tablerouser[y+1,x-1]='  '
                tablerouser[y+2,x-2]="⚪"
                y=y+2
                x=x-2

            elif tablero[y+1,x+1]>2 and tablero[y+2,x+2]==0:
                tablero[y,x]=0
                tablero[y+1,x-1]=0
                tablero[y+2,x-2]=1
                tablerouser[y,x]='  '
                tablerouser[y+1,x-1]='  '
                tablerouser[y+2,x-2]="⚪"
                y=y+2
                x=x+2
            else:
                flag=True

        if x<2 and y+2<=7:
            if tablero[y+1,x+1]>2 and tablero[y+2,x+2]==0:
                tablero[y,x]=0
                tablero[y+1,x+1]=0
                tablero[y+2,x+2]=1
                tablerouser[y,x]='  '
                tablerouser[y+1,x+1]='  '
                tablerouser[y+2,x+2]="⚪"
                y=y+2
                x=x+2

            else:
                flag=True
        else:
            flag=True

def rangoDama(x,y,mov,cantidad):