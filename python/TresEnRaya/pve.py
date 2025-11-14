import pvp
from tabulate import tabulate
import fGenerales
import random as rd

def pve(tablero,tableroJug,win1,win2):#Funcion para definir el proceso del juego
    print(tabulate(tableroJug, tablefmt="rounded_grid"))
    win1=pvp.j1(tablero,tableroJug)
    if win1==False:
        win2=engine(tablero,tableroJug)
    return win1, win2

def engine(tablero,tableroJug):#Funcion para colocar de manera random las fichas de la maquina
    x=rd.randint(0,2)
    y=rd.randint(0,2)
    if tablero[y][x]==0:
        tablero[y][x]=2
        tableroJug[y][x]="O"
        print(tabulate(tableroJug, tablefmt="rounded_grid"))
        win2=fGenerales.comrpobarJ2(tablero)
    else:
        win2=engine(tablero,tableroJug)
    return win2