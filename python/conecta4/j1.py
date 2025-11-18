#Importamos librerias
import c4_core as cc

#Definmos funciones
def turnoJ1(tablero,tableroUser,cantidadcol, cantidaFil,win1,win2):#Funcion donde definimos las opciones del turno 1
    colocado=False
    jug=1
    while colocado==False:
        x=input(f"¿En que columna quieres poner tu ficha? Las columnas van del 0 al {cantidadcol-1} " \
        "de izquierda a derecha.\n")
        x=cc.esNumerico(x)
        while x>=cantidadcol:
            x=input(f"Columna fuera de rango, recuerda poner numeros del 0 al {cantidadcol-1}. Elige de nuevo\n")
            x=cc.esNumerico
        for i in range(cantidaFil):
            if tablero[(cantidaFil-i-1),x]==0 and colocado==False:
                tablero[(cantidaFil-i-1),x]=1
                tableroUser[(cantidaFil-i-1),x]="🔴"
                colocado=True
        if colocado==False:
            print("No se ha podido colocar la pieza, prueba de nuevo")
    win1,win2=cc.winJugador(tablero,cantidadcol,cantidaFil,jug,win1,win2)
            
    cc.mostrarTabl(tableroUser)
    return win1,win2
