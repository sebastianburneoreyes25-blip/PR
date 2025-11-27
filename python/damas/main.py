#Importamos librerias
import numpy as np
import damas_core as dc

#Definimos variables
tablero=np.zeros((8,8))
tableroUser=np.full((8,8), '  ')
pJ1=1
dJ1=2
pJ2=3
dJ2=4


#Logica de programacion
dc.inicioJuego(tablero,tableroUser)
