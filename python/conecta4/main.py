#Importamos librerias
import numpy as np
import c4_core as cc
import j1
import j2



#Definimos varibales
cantidadCol=7
cantidadFilas=6
tablero=np.zeros((cantidadFilas,cantidadCol))
tableroUser=np.full((cantidadFilas,cantidadCol), "-")
win1=False
win2=False



#Logica de programación
cc.bienvenida()

while win1==False and win2==False and (tablero==0).any():
    win1,win2=j1.turnoJ1(tablero,tableroUser,cantidadCol, cantidadFilas,win1,win2)
    if win1==False:
        win1,win2=j2.turnoJ2(tablero,tableroUser,cantidadCol, cantidadFilas,win1,win2)
if win1==True:
        print("Felicidades jugador Rojo, ¡HAS GANADO!")
elif win2==True:
        print("Felicidades jugador Azul, ¡HAS GANADO!")
elif win1==False and win2==False and (tablero!=0).all():
        print("Estamos ante un empate. Juega de nuevo para desempatar :)")


