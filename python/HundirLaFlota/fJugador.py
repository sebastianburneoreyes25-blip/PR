#Importamos librerias
import numpy as np

#Definimos funciones 
def tiro(tablero,tableroBarcos,intentos,s):#Funcion para definir la cordenada a comprobar si hay o no un barco
    print(f"{tablero}\nLa cordenada 0,0 se encuentra en la esquina superior izquierda.\nEscribe 111 para el menu de guardado y salir del juego.")
    x=input("Intoduce la columna en la que disparar. La cordenada tiene que ser numerica del 0 al 19.\n")
    x=esNumerico(x)
    if x==111:#Menu del juego
        s=input("1.Guardar y salir.\n2.Continuar.\n")
        s=esNumerico(s)
        match s:
            case 1:
                print("Partida guardada. Hasta la proxima!")
            case 2:
                print("Continuando")
            case _:
                print("No se entendio el comando, continuaremos la partida.")
    elif x!=111 and s!=1:
        while x>19 or x<0:
            x=comrpobarPos(x)
        y=input("Intoduce la fila en la que disparar. La cordenada tiene que ser numerica del 0 al 19.\n")
        y=esNumerico(y)
        while y>19:
            y=comrpobarPos(y)

        intentos=impacto(tableroBarcos,x,y,tablero,intentos)
    return intentos,s

def comrpobarPos(a):#Funcion para comprobar que la cordenada puesta sea en el rango
    a=input("Tiene que serdel 0 al 19, no puede ser mayor ni menor\n")
    a=esNumerico(a)
    return a

def esNumerico(a):#Funcion para comprobar que sea numerico
    while a.isalpha():
        a=("La cordenada tiene que ser numerica del 0 al 19.\n")
    a=int(a)
    return a

def impacto(tableroB,x,y,tableroUser,intentos):#Funcion para comprobar si impacta en el barco

    if tableroB[y][x]==0 and tableroUser[y][x]==0:
        print("¡AGUA! Intentalo de nuevo")
        tableroUser[y,x]=3
        tableroB[y,x]=3
        intentos+=1
    elif tableroB[y][x]==1 and tableroUser[y][x]==0:
        print("¡Tocado!")    
        tableroUser[y,x]=2
        tableroB[y,x]=2
        intentos+=1
    elif tableroUser[y][x]!=0:
        print("Esa posicion ya se comprobo anteriormente.")

    return intentos

def bienvenida():#Funcion para dar la bienvenida
    print("¡Bienvenido a Hundir la Flota!\n" \
    "El tablero va del 0 a 19 tanto en Horizontal como Vertical, siempre antes de empezar un tiro tendras la oportunidad de guardar la partida o salir del juego.\n" \
    "Hay 3 barcos, uno de dos bloques, otro de 3 y el ultimo de 4. ¡Mucha suerte y pasalo bien!")

def finJuego(intentos):#Funcion para mostrar en cuantos intentos se ha completdo el juego
    print(f"¡Has derribado la flota enemiga en {intentos} intentos! Enhorabuena")