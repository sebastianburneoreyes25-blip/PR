#Importamos librerias
import numpy as np
from tabulate import tabulate
import c4_core as cc
import j1



#Definimos varibales
cantidadCol=7
cantidadFilas=6
tablero=np.zeros((cantidadFilas,cantidadCol))
tableroUser=np.full((cantidadFilas,cantidadCol), "-")


#Logica de programación
cc.bienvenida()
j1.turnoJ1(tablero,tableroUser,cantidadCol, cantidadFilas)

