#Importamos librerias
from tabulate import tabulate 
import pvp
import pve
import numpy as np
#Definimos funciones
    
def bienvenida(a):
    print("Bienvenido al 3 en raya. hay dos modalidades, PVP o PVE" )
    a=input("Para jugar PVP(personaVSpersona) presiona 0. Para jugar PVE(PersonaVSMaquina) presiona 1.\n")
    a=esNumerico(a)
    while a<0 or a>1:
        a=input("Debemos elegir 0 o 1\n")
        a=esNumerico(a)

    return a

def esNumerico(a):
    while a.isalpha():
        a=input("El comando debe ser un numero.\n")
    a=int(a)
    return a

def tipoJuego(a,tablero,tableroJug,win1,win2):
    if a==0:
        while win1==False and win2==False and (tablero==0).any():
            win1,win2=pvp.pvp(tablero,tableroJug,win1,win2)
    elif a==1:
        while win1==False and win2==False and (tablero==0).any():
            win1,win2=pve.pve(tablero,tableroJug,win1,win2)
    return win1,win2

def comrpobarJ1(tablero):
    win1=False
    diagonal=np.diag(tablero)
    diagonalInversa=np.fliplr(tablero).diagonal()
    for i in range (3):
        if (tablero[i-1,:].all()==1 ):
            win1=True
    for i in range (3):
        if (tablero[:,i-1].all()==1 ):
            win1=True 
    if (diagonal.all()==1):
        win1=True
    if (diagonalInversa.all()==1):
        win1=True

    return win1

def comrpobarJ2(tablero):
    win2=False
    diagonal=np.diag(tablero)
    diagonalInversa=np.fliplr(tablero).diagonal()
    for i in range (3):
        if (tablero[i-1,:].all()==2 ):
            win2=True
    for i in range (3):
        if (tablero[:,i-1].all()==2 ):
            win2=True
    if diagonal.all()==2:
        win2=True
    if (diagonalInversa.all()==2):
        win2=True
    
    return win2

def resultado(tablero,win1,win2,tipo):
    if (tablero==0).any() and win1==False and win2==False:
        print("¡Empate!")
    elif win1==True:
        print("Ha ganado el jugador 1")
    elif win2==True:
        if tipo==0:
            print("Ha ganado el jugador 2")
        elif tipo==1:
            print("Ha ganado la maquina.")