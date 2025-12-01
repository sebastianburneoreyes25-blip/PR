#importamos librerias
import damas_core

#Definimos funciones
def movimientosJ2(tablero,x,y,movValido,tablerouser):
    if tablero[y,x]==3 or tablero[y,x]==4:
        if tablero[y,x]==3:#Si la casilla seleccionada tiene un peon se realiza este código
            while movValido==False:
                rangoVal=False
                while rangoVal==False:#Hasta que el jugador no ponga un rango especifico no se podra salir del bucle
                    mov=input("Puedes mover la ficha en diagonal hacia arriba. Presiona 0 para la izquierda, 1 para la derecha\n")
                    mov=damas_core.esNumerico(mov)
                    rangoVal=rangoPeon(x,y,mov)
                    if rangoVal==False:
                        print("El rango elegido no es valido. Prueba de nuevo")
                if mov==0 :#Realizamos el movimiento, borrando el valor de la posicion anterior en el tablero y tableroUser
                    if tablero[y-1,x-1]==0:
                        tablero[y,x]=0
                        tablero[y-1,x-1]=1
                        tablerouser[y,x]='  '
                        tablerouser[y-1,x-1]="⚫"
                        x=x-1
                        y=x-1
                        comprobacionPeon(x,y,tablero,tablerouser)#comprobamos que el peon coma de manera automatica si puede
                        movValido=True
                        damas_core.tranformacion(x,y,tablero,tablerouser)
                elif mov==1 :
                        if tablero[y-1,x+1]==0:
                            tablero[y,x]=0
                            tablero[y-1,x+1]=1
                            tablerouser[y,x]='  '
                            tablerouser[y-1,x+1]="⚫"
                            x=x+1
                            y=y-1
                            comprobacionPeon(x,y,tablero,tablerouser)#comprobamos que el peon coma de manera automatica si puede
                            movValido=True
                            damas_core.tranformacion(x,y,tablero,tablerouser)
            if tablero[y,x]==4:#Si la casilla seleccionada tiene una dama del jugador 2, se realiza este código
                while movValido==False:
                    rangoVal=False
                    while rangoVal==False:#Hasta que el jugador no ponga un rango especifico no se podra salir del bucle
                        movHorizontal=damas_core.esNumerico(input("Puedes mover la ficha en diagonal hacia abajo. Presiona 0 para la izquierda, 1 para la derecha\n"))
                        movVertical=damas_core.esNumerico(input("Puedes mover la dama hacia arriba (0) o abajo(1)\n"))
                        cantidad=damas_core.esNumerico(input("¿Que cantidad de casillas quieres moverte?"))
                        rangoVal=rangoDama(x,y,movHorizontal,movVertical,cantidad)
                        if rangoVal==False:
                            print("El rango elegido no es valido. Prueba de nuevo")
                    if movHorizontal==0 and movVertical==1:#Realizamos el movimiento, borrando el valor de la posicion anterior en el tablero y tableroUser
                        if tablero[y-cantidad,x-cantidad]==0:
                            tablero[y,x]=0
                            tablero[y-cantidad,x-cantidad]=1
                            tablerouser[y,x]='  '
                            tablerouser[y-cantidad,x-cantidad]="⚫"
                            x=x-cantidad
                            y=y-cantidad
                            comprobacionDama(x,y,tablero,tablerouser)

                    if movHorizontal==1 and movVertical==1:
                        if tablero[y-cantidad,x+cantidad]==0:
                            tablero[y,x]=0
                            tablero[y-cantidad,x+cantidad]=1
                            tablerouser[y,x]='  '
                            tablerouser[y-cantidad,x+cantidad]="⚫"
                            x=x+cantidad
                            y=y-cantidad
                            comprobacionDama(x,y,tablero,tablerouser)

                    if movHorizontal==1 and movVertical==0:
                        if tablero[y-cantidad,x+cantidad]==0:
                            tablero[y,x]=0
                            tablero[y-cantidad,x+cantidad]=1
                            tablerouser[y,x]='  '
                            tablerouser[y-cantidad,x+cantidad]="⚫"
                            x=x+cantidad
                            y=y-cantidad
                            comprobacionDama(x,y,tablero,tablerouser)

                    if movHorizontal==0 and movVertical==0:
                        if tablero[y-cantidad,x-cantidad]==0:
                            tablero[y,x]=0
                            tablero[y-cantidad,x-cantidad]=1
                            tablerouser[y,x]='  '
                            tablerouser[y-cantidad,x-cantidad]="⚫"
                            x=x-cantidad
                            y=y-cantidad
                            comprobacionDama(x,y,tablero,tablerouser)



def rangoPeon(x,y,mov):#Funcion que nos comprobará si se puede hacer el movimiento(si no se sale del tablero)
    rangoVal=False
    if mov==0:
        if x-1>=0 and y-1>=0:
            rangoVal=True
    if mov==1 and y-1>=0:
        if x+1<=7:
            rangoVal=True
    return rangoVal

def comprobacionPeon(x,y,tablero,tablerouser):#Hará la comprobación de que el peon como automaticamente si tiene una ficha en sus diagonales y un espacio vacio donde moverse.
    flag=False
    while flag==False:
        #Dependiendo de en que columna se encuentre el peon vera una o dos posibilidades para comer, si esta en la columna 1 no podrá directamente comer hacia la izquierda por el tamaño del tablero
        #y por el moviemiento(se mueve dos hacia arriba e izquierda/derecha)
        if x>=2 and y-2>=0:
            if tablero[y-1,x-1]<3 and tablero[y-2,x-2]==0:
                tablero[y,x]=0
                tablero[y-1,x-1]=0
                tablero[y-2,x-2]=1
                tablerouser[y,x]='  '
                tablerouser[y-1,x-1]='  '
                tablerouser[y-2,x-2]="⚫"
                y=y-2
                x=x-2

            elif tablero[y-1,x+1]<3 and tablero[y-2,x+2]==0:
                tablero[y,x]=0
                tablero[y-1,x-1]=0
                tablero[y-2,x-2]=1
                tablerouser[y,x]='  '
                tablerouser[y-1,x-1]='  '
                tablerouser[y-2,x-2]="⚫"
                y=y-2
                x=x+2
            else:#Si no puede comer entrara aqui para cambiar la variable flag y salir del bucle
                flag=True

        if x<2 and y-2>=0:
            if tablero[y-1,x+1]<3 and tablero[y-2,x+2]==0:
                tablero[y,x]=0
                tablero[y-1,x+1]=0
                tablero[y-2,x+2]=1
                tablerouser[y,x]='  '
                tablerouser[y-1,x+1]='  '
                tablerouser[y-2,x+2]="⚫"
                y=y-2
                x=x+2

            else:#Si no puede comer entrara aqui para cambiar la variable flag y salir del bucle
                flag=True
        else:#Si no puede comer entrara aqui para cambiar la variable flag y salir del bucle
            flag=True

def comprobacionDama(x,y,tablero,tablerouser):
    flag=False
    while flag==False:
        #Dependiendo de en que columna se encuentre la dama vera las posibilidades para comer, si esta en la columna 1 no podrá directamente comer hacia la izquierda por el tamaño del tablero
        #y por el moviemiento(se mueve dos hacia abajo/arriba e izquierda/derecha)
        if x>=2 and y+2<=7:#Podra comer en todas las direcciones diagonales
            if tablero[y+1,x-1]<3 and tablero[y+2,x-2]==0:#Hacia abajo izq
                tablero[y,x]=0
                tablero[y+1,x-1]=0
                tablero[y+2,x-2]=2
                tablerouser[y,x]='  '
                tablerouser[y+1,x-1]='  '
                tablerouser[y+2,x-2]="⚫D"
                y=y+2
                x=x-2
            elif tablero[y-1,x-1]<3 and tablero[y-2,x-2]==0:#Hacia arriba izq
                tablero[y,x]=0
                tablero[y-1,x-1]=0
                tablero[y-2,x-2]=2
                tablerouser[y,x]='  '
                tablerouser[y-1,x-1]='  '
                tablerouser[y-2,x-2]="⚫D"
                y=y+2
                x=x-2
            elif tablero[y-1,x+1]<3 and tablero[y-2,x+2]==0:#Hacia arriba derecha
                tablero[y,x]=0
                tablero[y-1,x+1]=0
                tablero[y-2,x+2]=2
                tablerouser[y,x]='  '
                tablerouser[y-1,x+1]='  '
                tablerouser[y-2,x+2]="⚫D"
                y=y+2
                x=x-2
            elif tablero[y+1,x+1]<3 and tablero[y+2,x+2]==0:#Hacia abajo derecha
                tablero[y,x]=0
                tablero[y+1,x-1]=0
                tablero[y+2,x-2]=2
                tablerouser[y,x]='  '
                tablerouser[y+1,x-1]='  '
                tablerouser[y+2,x-2]="⚫D"
                y=y+2
                x=x+2
            else:#Si no puede comer entrara aqui para cambiar la variable flag y salir del bucle
                flag=True

        if x<2 and y+2<=7:#Por el tamaño del tablero solo puede comer en las diagonales derechas(arriba y abajo)
            if tablero[y+1,x+1]<3 and tablero[y+2,x+2]==0:
                tablero[y,x]=0
                tablero[y+1,x+1]=0
                tablero[y+2,x+2]=2
                tablerouser[y,x]='  '
                tablerouser[y+1,x+1]='  '
                tablerouser[y+2,x+2]="⚫D"
                y=y+2
                x=x+2
            elif tablero[y-1,x+1]<3 and tablero[y-2,x+2]==0:
                tablero[y,x]=0
                tablero[y-1,x+1]=0
                tablero[y-2,x+2]=2
                tablerouser[y,x]='  '
                tablerouser[y-1,x+1]='  '
                tablerouser[y-2,x+2]="⚫D"
                y=y+2
                x=x+2

            else:#Si no puede comer entrara aqui para cambiar la variable flag y salir del bucle
                flag=True
        else:#Si no puede comer entrara aqui para cambiar la variable flag y salir del bucle
            flag=True

def rangoDama(x,y,movHorizontal,movVertical,cantidad):#Funcion para comprobar que la dama no se salga del tablero
    rangoValido=False
    if movHorizontal==0 and x-cantidad>=0:
        if movVertical==0 and y-cantidad>=0:
            rangoValido=True
        if movVertical==1 and y+cantidad<=7:
            rangoValido=True
    if movHorizontal==1 and x+cantidad<=7:
        if movVertical==0 and y-cantidad>=0:
            rangoValido=True
        if movVertical==1 and y+cantidad<=7:
            rangoValido=True
    return rangoValido