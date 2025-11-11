#Importamos librerias
import numpy as np
import random as rd

#Definimos funciones
def posInicial(barco,tablero,eje):#Funcion para estableces la cordenada de inicio teniendo en cuenta el tamaño del barco
    a=len(barco)
    if eje==0:
                inicioX=rd.randint(0,20-a)         
                inicioY=rd.randint(0,20-a)
                while max(tablero[inicioX+i,inicioY]!=0 for i in range (a)):#Con este while (donde se comprueba mas de una posicion con el for) evitamos solapamientos.
                    inicioX=rd.randint(0,20-a)         
                    inicioY=rd.randint(0,20-a)
    elif eje==1:
                inicioX=rd.randint(0,20-a)         
                inicioY=rd.randint(0,20-a)
                while max(tablero[inicioX,inicioY+i]!=0 for i in range (a)):
                    inicioX=rd.randint(0,20-a)         
                    inicioY=rd.randint(0,20-a)
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
                    tablero[x+n,y]=1
                    n+=1    
        case 3:
                n=1
                tablero[x,y]=1
                while n!=3:
                    tablero[x+n,y]=1
                    n+=1

        case 4:
                n=1
                tablero[x,y]=1
                while n!=4:
                    tablero[x+n,y]=1
                    n+=1

    return tablero
    
def barcoY(barco,tablero,x,y):#Funcion para esconderlo en el eje Y(Se coloca en vertical)
    a=len(barco)
    match a:
        case 2:
                n=1
                tablero[x,y]=1
                while n!=2:
                    tablero[x,y+n]=1
                    n+=1

        case 3:
                n=1
                tablero[x,y]=1
                while n!=3:
                    tablero[x,y+n]=1
                    n+=1
        case 4:
                n=1
                tablero[x,y]=1
                while n!=4:
                    tablero[x,y+n]=1
                    n+=1

    return tablero

def esconderBarco(barco,tablero):#Funcion para esconder los barcos
    eje=rd.randint(0,1)
    inicioX,inicioY=posInicial(barco,tablero,eje)
    modTablero(tablero,inicioX,inicioY, eje,barco)

def startGame(b1,b2,b3,tablero):#Funcion que se ejecutara al empezar el juego
    esconderBarco(b1, tablero)
    esconderBarco(b2, tablero)
    esconderBarco(b3, tablero)


    
    
