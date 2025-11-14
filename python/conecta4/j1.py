
import colorama
import c4_core as cc

def turnoJ1(tablero,tableroUser,cantidadcol, cantidaFil):
    x=input(f"¿En que columna quieres poner tu ficha? Las columnas van del 0 al {cantidadcol-1} " \
    "de izquierda a derecha.\n")
    x=cc.esNumerico(x)
    while x>=cantidadcol:
        x=input(f"Columna fuera de rango, recuerda poner numeros del 0 al {cantidadcol-1}. Elige de nuevo\n")
        x=cc.esNumerico
    colocado=False
    for i in range(cantidaFil):
        if tablero[i-1,x]==0 and colocado==False:
            tablero[i-1,x]=1
            tableroUser[i-1,x]="J1"
            colocado=True
            
    print(tableroUser)
