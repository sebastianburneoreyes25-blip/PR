#imporamos librerias
import j1
import numpy as np
from tabulate import tabulate
import j2

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

def juego(jug,tablero,tableroUser):
   flag=False
   while flag==False: 
        mostrarTablero(tableroUser)
        y=input("¿En que fila esta la ficha que vas a mover?\n")
        y=esNumerico(y)
        x=input("¿En que columna esta la ficha que vas a mover?\n")
        x=esNumerico(x)
        flag=comprobarFicha(jug,tablero,y,x,flag)
        if flag==True:
            moverFicha(tablero,y,x,jug,tableroUser)

def comprobarFicha(jug,tablero,y,x,flag):
    if jug==1:
        if tablero[y,x]==1 or tablero[y,x]==2:
            flag=True
    if jug==2:
        if tablero[y,x]==3 or tablero[y,x]==4:
            flag=True
    return flag

def moverFicha(tablero,y,x,jug,tableroUser):
    movValido=False
    if jug==1:
        j1.movimientosJ1(tablero,x,y,movValido,tableroUser)
    if jug==2:
        j2.movimientosJ2(tablero,x,y,movValido,tableroUser)

def esNumerico(a):#Funcion para comprobar que un dato introducido es numérico
    while a.isalpha():
        a=input("El valor debe de ser numerico. Prueba de nuevo \n")
    a=int(a)
    return a

def tranformacion(x,y,tablero,tablerouser):#Funcion para ver si un peon se transforma en una dama.
    if y==0 and tablero[y,x]==3 :#Cuando un peon negro llegue a la posicion y=0 se convertira en una dama negra
            tablero [y,x]==4
            tablerouser[y,x]=="⚫D"
    if y==7 and tablero[y,x]==1:#Cuando un peon blanco llegue a la posicion y=7 se convertira en una dama blanca
        tablero [y,x]==2
        tablerouser[y,x]=="⚪D"
    