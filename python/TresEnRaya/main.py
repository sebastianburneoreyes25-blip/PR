#Importamos librerias
import numpy as np
from tabulate import tabulate
import fGenerales

#Definimos funciones
tablero=np.zeros((3,3))
tipo=9
tableroJug=np.full((3,3), "-")
win1=False
win2=False
#Logica de programacion
print(tabulate(tableroJug, tablefmt="rounded_grid"))
tipo=fGenerales.bienvenida(tipo)
win1,win2=fGenerales.tipoJuego(tipo,tablero, tableroJug,win1,win2)
fGenerales.resultado(tablero,win1,win2,tipo)

