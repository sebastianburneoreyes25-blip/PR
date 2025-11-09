#Importamos librerias
import numpy as np
import fBarcos
import fJugador

#Definimos variables
tableroUser=np.full((20,20),0)
tableroBarcos=np.full((20,20),0)
intentos=0
barco1=np.array([1,1])
barco2=np.array([1,1,1])
barco3=np.array([1,1,1,1])
n=0

#Logica de programacion
fBarcos.starGame(barco1,barco2,barco3,tableroBarcos)
print(tableroBarcos)
fJugador.bienvenida()
while (tableroBarcos==1).any():
    fJugador.tiro(tableroUser, tableroBarcos, intentos, n)
print("Hasta la vista")
