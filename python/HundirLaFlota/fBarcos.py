#Importamos librerias
import numpy as np
import random as rd

#Definimos funciones
def posInicial(barco,tablero,eje):#Funcion para estableces la cordenada de inicio teniendo en cuenta el tamaño del barco
    a=len(barco)
    if eje==0:
        match a:
            case 2:
                inicioX=rd.randint(0,18)         
                inicioY=rd.randint(0,18)
                while max(tablero[inicioX+i,inicioY]!=0 for i in range (a)):
                    inicioX=rd.randint(0,18)         
                    inicioY=rd.randint(0,18)
            case 3:
                inicioX=rd.randint(0,17)
                inicioY=rd.randint(0,17)
                while max(tablero[inicioX+i,inicioY]!=0 for i in range (a)):
                    inicioX=rd.randint(0,17)
                    inicioY=rd.randint(0,17)
            case 4:
                inicioX=rd.randint(0,16)
                inicioY=rd.randint(0,16)
                while max(tablero[inicioX+i,inicioY]!=0 for i in range (a)):
                    inicioX=rd.randint(0,16)
                    inicioY=rd.randint(0,16)
    elif eje==1:
         match a:
            case 2:
                inicioX=rd.randint(0,18)         
                inicioY=rd.randint(0,18)
                while max(tablero[inicioX,inicioY+i]!=0 for i in range (a)):
                    inicioX=rd.randint(0,18)         
                    inicioY=rd.randint(0,18)
            case 3:
                inicioX=rd.randint(0,17)
                inicioY=rd.randint(0,17)
                while max(tablero[inicioX,inicioY+i]!=0 for i in range (a)):
                    inicioX=rd.randint(0,17)
                    inicioY=rd.randint(0,17)
            case 4:
                inicioX=rd.randint(0,16)
                inicioY=rd.randint(0,16)
                while max(tablero[inicioX,inicioY+i]!=0 for i in range (a)):
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

def esconderBarco(barco,tablero):
    eje=rd.randint(0,1)
    inicioX,inicioY=posInicial(barco,tablero,eje)
    modTablero(tablero,inicioX,inicioY, eje,barco)

def starGame(b1,b2,b3,tablero):
    esconderBarco(b1, tablero)
    esconderBarco(b2, tablero)
    esconderBarco(b3, tablero)


    
    
