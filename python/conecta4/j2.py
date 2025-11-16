from tabulate import tabulate
import c4_core as cc


def turnoJ2(tablero,tableroUser,cantidadcol, cantidaFil,win1,win2):
    jug=2
    x=input(f"¿En que columna quieres poner tu ficha? Las columnas van del 0 al {cantidadcol-1} " \
    "de izquierda a derecha.\n")
    x=cc.esNumerico(x)
    while x>=cantidadcol:
        x=input(f"Columna fuera de rango, recuerda poner numeros del 0 al {cantidadcol-1}. Elige de nuevo\n")
        x=cc.esNumerico
    colocado=False
    for i in range(cantidaFil):
        if tablero[(cantidaFil-i-1),x]==0 and colocado==False:
            tablero[(cantidaFil-i-1),x]=2
            tableroUser[(cantidaFil-i-1),x]="🔵"
            colocado=True
    win1,win2=cc.winJugador(tablero,cantidadcol,cantidaFil,jug,win1,win2)

    cc.mostrarTabl(tableroUser)
    return win1,win2