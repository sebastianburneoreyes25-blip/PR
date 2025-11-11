from tabulate import tabulate
import fGenerales




def pvp(tablero,tableroJug,win1,win2):
    print(tabulate(tableroJug, tablefmt="rounded_grid"))
    win1=j1(tablero,tableroJug)
    if win1==False:
        win2=j2(tablero,tableroJug)
    return win1, win2


def j1(tablero, tableroJug):
    win1=False
    print("Para colocar una ficha deberemos poner sus cordenadas. Empieza en la esquina superior izquierda. \nLas cordenadas van del 0 al 2 tanto en el eje horizontal como vertical." \
    "\nEmpezamos con el J1(X)")

    x=input("Elige la columna en la que se pondra\n")
    x=fGenerales.esNumerico(x)
    x=comprobarCord(x)
    y=input("Elige la fila en la que se pondra\n")
    y=fGenerales.esNumerico(y)
    y=comprobarCord(y)
    if tablero[y,x]==0:
        tablero[y][x]=1
        tableroJug[y][x]="X"    
        print(tabulate(tableroJug, tablefmt="rounded_grid"))
        win1=fGenerales.comrpobarJ1(tablero)
    else:
        print("Elige de nuevo otra posicion")
        j1(tablero,tableroJug)
    return win1
    
def j2(tablero,tableroJug):
    print("Para colocar una ficha deberemos poner sus cordenadas. Empieza en la esquina superior izquierda. \nLas cordenadas van del 0 al 2 tanto en el eje horizontal como vertical." \
    "\nEmpezamos con el J2(O)")
    x=input("Elige la columna en la que se pondra\n")
    x=fGenerales.esNumerico(x)
    x=comprobarCord(x)
    y=input("Elige la fila en la que se pondra\n")
    y=fGenerales.esNumerico(y)
    y=comprobarCord(y)
    if tablero[y][x]==0:
        tablero[y][x]=2
        tableroJug[y][x]="O"
        print(tabulate(tableroJug, tablefmt="rounded_grid"))
        win2=fGenerales.comrpobarJ2(tablero)
    else:
        print("Elige de nuevo otra posicion")
        win2=j2(tablero,tableroJug)
    return win2

def comprobarCord(a):
    while a<0 or a>2:
        a=input("Las cordenadas validas van del 0 al 2 de izquierda a derecha. Elige de nuevo\n")
        a=fGenerales.esNumerico(a)
    return a

