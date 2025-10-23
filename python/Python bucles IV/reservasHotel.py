#Defino variables
habitaciones={
    1:("luxury", 500),
    2:("luxury", 500),
    3:("luxury", 500),
    4:("luxury", 500),
    5:("luxury", 500),
    6:("luxury", 500),
    7:("luxury", 500),
    8:("Matrimonio", 100),
    9:("Matrimonio", 100),
    10:("Matrimonio", 100),
    11:("Matrimonio", 100),
    12:("Matrimonio", 100),
    13:("Matrimonio", 100),
    14:("Matrimonio", 100),
    15:("Sencillo",50),
    16:("Sencillo",50),
    17:("Sencillo",50),
    18:("Sencillo",50),
    19:("Sencillo",50),
    20:("Sencillo",50),
    21:("Sencillo",50)
}

reservas=[]
eleccion=""
#Defino funciones
def mostrarMenu():
    print("1.Mostrar Habitaciones\n2.Reservar Habitación\n3.Ver Reservas\n4.Calcular total a pagar\n5.Salir\n")

def mostrarHab(habitaciones):
    for a,(b,c) in habitaciones.items():
        print(f"-Habitacion {a}: {b}  {c}€")

def reservar():
    mostrarHab(habitaciones)
    reserva=int(input("Pon el numero que quieres reservar.\n"))

    return reserva

def verReserca(reservas):
    for a in reservas:
        for x,(y,z) in habitaciones.items():
            if a==x:
               print(f"-Habitacion {x}, tipo {y} precio {z}€")

def calcularTotal():
    total=0
    for a in reservas:
        for x,(y,z) in habitaciones.items():
            if a==x:
                print(f"-Habitacion {x}, tipo {y} precio {z}€")
                total+=z
    
    return total


#Logica de programacion
mostrarMenu()
while eleccion!= "5":
    eleccion=input("Dime que quieres hacer.\n")
    match eleccion:
        case "1":
            mostrarHab(habitaciones)
    
        case "2":
            r=reservar()
            n=True
            for a,(b,c) in habitaciones.items():
                if r==a and a not in reservas:
                    reservas.append(r)
                elif r==a and a  in reservas:
                    print(f"\n La habitacion {a} ya está reservada.Elige otra habitacion\n")
                elif r not in habitaciones and n==True:
                    print(f"La habitacion {r} no existe. Prueba de nuevo.")
                    n=False

        case "3":
            verReserca(reservas)

        case "4":
            print(f"El total a pagar es {calcularTotal()}€")

        case "5":
            print("Sayonara baby!!")
        case _:
            print("No entendi el comando, repitemelo por favor.")
