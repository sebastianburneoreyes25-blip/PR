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
    if (tablero==3).any() or (tablero==4).any():#Si en el tablero hay fichas del j2 será el tueno del J1
        print("Turno del J2")
        jug=2
        dc.juego(jug,tablero,tableroUser)
        if  (tablero==1).any() or (tablero==2).any():#Si en el tablerop hay fichas del j1 sera el turno del j2
            print("Turno del J1")
        else:#Si no hay fichas del j1 gana el j2
            fin=True
            win=2
    else:#Si no hay fichas del j2 gana el j1
        fin=True
        win=1
match win:
    case 1:
        print("Felicidades J1 has ganado!!!")
    case 2:
        print("Felicidades J2 has ganado!!!")

        
