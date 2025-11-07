#Importamos librerias
import numpy as np
import random as rd

#Definimos funciones
def posInicial(barco,tablero,eje):#Funcion para estableces la cordenada de inicio teniendo en cuenta el tamaño del barco
    a=len(barco)
    match a:
        case 2:
            inicioX=rd.randint(0,18)         
            inicioY=rd.randint(0,18)
                        while tablero[inicioX+1,inicioY]==1 or tablero[inicioX,inicioY+1]==1:
        case 3:
            inicioX=rd.randint(0,17)
            inicioY=rd.randint(0,17)
        case 4:
            inicioX=rd.randint(0,16)
            inicioY=rd.randint(0,16)
    return inicioX, inicioY

def modTablero(tablero, x,y, eje, barco):#Modificamos el tablero para esconder los barcos
    if eje==0:
        tablero=barcoX(barco,tablero,x,y)
    elif eje==1:
        tablero=barcoY(barco,tablero,x,y)

        

def barcoX(barco,tablero,x,y):#Funcion para esconderlo en el eje X(Se coloca en horizontal)
    a=len(barco)
    match a:
        case 2:
                n=1
                tablero[x,y]=1
                while n!=2:
                    tablero[x+1,y]=1
                    n+=1
        case 3:
                n=1
                tablero[x,y]=1
                while n!=3:
                    tablero[x+1,y]=1
                    n+=1
        case 4:
                n=1
                tablero[x,y]=1
                while n!=4:
                    tablero[x+1,y]=1
                    n+=1
    return tablero
    
def barcoY(barco,tablero,x,y):#Funcion para esconderlo en el eje Y(Se coloca en vertical)
    a=len(barco)
    match a:
        case 2:
                n=1
                tablero[x,y]=1
                while n!=2:
                    tablero[x,y+1]=1
                    n+=1
        case 3:
                n=1
                tablero[x,y]=1
                while n!=3:
                    tablero[x,y+1]=1
                    n+=1
        case 4:
                n=1
                tablero[x,y]=1
                while n!=4:
                    tablero[x,y]+1=1
                    n+=1
    return tablero

def esconderBarco(barco,tablero):
    eje=rd.randint(0,1)
    inicioX,inicioY=posInicial(barco)
    modTablero(tablero,inicioX,inicioY, eje,barco)


    
    
