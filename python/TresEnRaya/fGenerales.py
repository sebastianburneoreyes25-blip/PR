#Importamos librerias
from tabulate import tabulate 
import pvp
import pve
import numpy as np
#Definimos funciones
    
def bienvenida(a):#Funcion para dar la bienvenida y obtener que tipo de juego empezamos
    print("Bienvenido al 3 en raya. hay dos modalidades, PVP o PVE" )
    a=input("Para jugar PVP(personaVSpersona) presiona 0. Para jugar PVE(PersonaVSMaquina) presiona 1.\n")
    a=esNumerico(a)
    while a<0 or a>1:
        a=input("Debemos elegir 0 o 1\n")
        a=esNumerico(a)

    return a

def esNumerico(a):#Funcion para comprobar que es numero
    while a.isalpha():
        a=input("El comando debe ser un numero.\n")
    a=int(a)
    return a

def tipoJuego(a,tablero,tableroJug,win1,win2):#En dependecia del juego se ejecuta un codigo u otro
    if a==0:
        while win1==False and win2==False and (tablero==0).any():
            win1,win2=pvp.pvp(tablero,tableroJug,win1,win2)
    elif a==1:
        while win1==False and win2==False and (tablero==0).any():
            win1,win2=pve.pve(tablero,tableroJug,win1,win2)
    return win1,win2

def comrpobarJ1(tablero):#Comprobamos si el J1 ha ganado
    win1=False
    diagonal=np.diag(tablero)
    diagonalInversa=np.fliplr(tablero).diagonal()
    for i in range (3):
        if (tablero[i-1,:].all()==1 ):
            win1=True
    for i in range (3):
        if (tablero[:,i-1].all()==1 ):
            win1=True 
    if np.all(np.diag(tablero)==1):
        win1=True 
    if np.all(diagonalInversa==1):
        win1=True
    return win1

def comrpobarJ2(tablero):#Comprobamos si el J2 ha ganado
    win2=False
    diagonal=np.diag(tablero)
    diagonalInversa=np.fliplr(tablero).diagonal()
    for i in range (2):
        if (tablero[i,:].all()==2 ):
            win2=True
    for i in range (2):
        if (tablero[:,i].all()==2 ):
            win2=True
    if np.all(diagonal==1):
        win2=True
    if np.all(diagonalInversa==2):
        win2=True
    
    return win2

def resultado(tablero,win1,win2,tipo):#Decimos si ha habido empate o hemos ganado
    if (tablero==0).any() and win1==False and win2==False:
        print("¡Empate!")
    elif win1==True:
        print("Ha ganado el jugador 1")
    elif win2==True:
        if tipo==0:
            print("Ha ganado el jugador 2")
        elif tipo==1:
            print("Ha ganado la maquina.")