#imporamos librerias

import numpy as np
from tabulate import tabulate

#Definimos funciones
def mostrarTablero(tablero):
    print("     0    1    2    3    4    5    6    7")
    for i in range (8):
        print(f"{i} {(tablero[i,:])}")

def inicioJuego(tablero,tablerouser):
    for y in range(3):
        for x in range(8):
            if (x+y)%2==0:
                tablero[y,x]=1
                tablerouser[y,x]="⚪"
    for y in range(3):
        for x in range(8):
            if (x+y+5)%2==0:
                tablero[y+5,x]=3
                tablerouser[y+5,x]='⚫'

def movimiento(jug,tablero):
    ()

