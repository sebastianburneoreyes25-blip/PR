#importamos
from tabulate import tabulate
import numpy as np

#Definimos funciones

def bienvenida():#Funcion de dar la bienvenida
    print("Bienvenido a conecta 4 donde el objetivo es meter una pieza en una columna y conectar 4. El Jugador 1(J1) seran fichas rojas y el jugador 2(J2) seran fichas azules ")


def esNumerico(a):#Funcion para asegurarnos que es un numero
    while a.isalpha():
        a=input("Debe ser un valor numerico\n")
    a=int(a)
    return a

def mostrarTabl(tableroUser):#Mostrar tablero con tabulate
    print(tabulate(tableroUser, tablefmt="fancy_grid"))

def winJugador(tablero,cantidadcol,cantidadfil,jug,win1,win2):#funcion donde determinara si el jugador que acaba de poner ficha ha ganado o no.
    for y in range(cantidadfil):
        for x  in range(cantidadcol):
            if tablero[cantidadfil-y-1,x]==jug:
                if y<cantidadfil-4 :
                    n=cantidadfil-y
                    if x<cantidadcol-4:
                        submatriz=tablero[n-4:n,x:x+4]
                    elif x>=cantidadcol-4:
                        submatriz=tablero[n-4:n,cantidadcol-4:cantidadcol]                                        
                    for i in range (4):
                        if np.all(submatriz[i-1,:]==jug):
                            if jug==1:
                                win1=True
                            if jug==2:
                                win2=True
                        if np.all(submatriz[:,i-1]==jug):
                            if jug==1:
                                win1=True
                            if jug==2:
                                win2=True
                    if y<3:
                        if np.all(np.fliplr(submatriz).diagonal()==jug):
                            if jug==1:
                                win1=True
                            if jug==2:
                                win2=True
                        if np.all(np.diag(submatriz)==jug):
                            if jug==1:
                                win1=True
                            if jug==2:
                                win2=True
    return win1, win2
