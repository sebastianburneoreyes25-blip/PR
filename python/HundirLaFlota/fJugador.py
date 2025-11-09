#Importamos librerias
import numpy as np


def tiro(tablero,tableroBarcos,intentos,n):
    s=0
    print(f"{tablero}\nLa cordenada 0,0 se encuentra en la esquina superior izquierda.\nEscribe 111 para el menu de guardado y salir del juego.")
    x=input("Intoduce la columna en la que disparar. La cordenada tiene que ser numerica del 0 al 19.")
    x=esNumerico(x)
    if x==111:
        s=input("1.Guardar y salir.\n2.Continuar.\n")
        match s:
            case 1:
                print("Partida guardada. Hasta la proxima!")
            case 2:
                print("Continuando")
            case _:
                print("No se entendio el comando, continuaremos la partida.")
    elif x!=111 and s!=1:
        y=input("Intoduce la fila en la que disparar. La cordenada tiene que ser numerica del 0 al 19.")
        y=esNumerico(y)
        n,intentos=impacto(tableroBarcos,x,y,tablero,n,intentos)

def esNumerico(a):
    while a.isalpha():
        a=("La cordenada tiene que ser numerica del 0 al 19.")
    a=int(a)
    return a

def impacto(tableroB,x,y,tableroUser,n,intentos):

    if tableroB[y][x]==0 and tableroUser[y][x]==0:
        print("¡AGUA! Intentalo de nuevo")
        tableroUser[y,x]=3
        tableroB[y,x]=3
        intentos+=1
    elif tableroB[y][x]==1 and tableroUser[y][x]==0:
        print("¡Tocado!")    
        tableroUser[y,x]=2
        tableroB[y,x]=2
        n+=1
        intentos+=1
    elif tableroUser[y][x]!=0:
        print("Esa posicion ya se comprobo anteriormente.")

    return n,intentos



def bienvenida():
    print("¡Bienvenido a Hundir la Flota!\n" \
    "El tablero va del 0 a 19 tanto en Horizontal como Vertical, siempre antes de empezar un tiro tendras la oportunidad de guardar la partida o salir del juego.\n" \
    "Hay 3 barcos, uno de dos bloques, otro de 3 y el ultimo de 4. ¡Mucha suerte y pasalo bien!")
