#importamos
import colorama

#Definimos funciones
def bienvenida():
    print("Bienvenido a conecta 4 donde el objetivo es meter una pieza en una columna y conectar 4. El Jugador 1(J1) seran fichas rojas y el jugador 2(J2) seran fichas azules ")


def esNumerico(a):
    while a.isalpha():
        a=input("Debe ser un valor numerico\n")
    a=int(a)
    return a

def mostrarTabl(tableroUser):
    for i in tableroUser:
        for x in i:
            if x=='J1':
                print(colorama.Fore.RED+x+colorama.Style.RESET_ALL)
