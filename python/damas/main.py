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
fin=False
jug=0
win=0
#Logica de programacion
dc.inicioJuego(tablero,tableroUser)

while fin!=True:
    jug=1
    dc.juego(jug,tablero,tableroUser)
    if (tablero==3).any() or (tablero==4).any():
        print("Turno del J2")
        jug=2
        dc.juego(jug,tablero,tableroUser)
        if  (tablero==1).any() or (tablero==2).any():
            print("Turno del J1")
        else:
            fin=True
            win=2
    else:
        fin=True
        win=1
match win:
    case 1:
        print("Felicidades J1 has ganado!!!")
    case 2:
        print("Felicidades J2 has ganado!!!")

        
