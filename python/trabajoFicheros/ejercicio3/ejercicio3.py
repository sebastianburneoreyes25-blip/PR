from pathlib import Path
import pickle as pkl

#Definimos variables
base=Path(__file__).resolve().parent #Esta variable nos dira la ruta donde se este ejecutando el gestor, y .parent cogera solamente el padre, es decir,
                                     #la carpeta donde esté el pograma independientemente del dispositivo o del SO.
ruta=base/"alumnos.pkl"
notasAlumnos={}
nombre=""
nombre_up=nombre.upper()
nota=0
terminar=False
#Logica de programacion
while nombre_up!="FIN":
    nombre=input("Dame el nombre del alumno a registrar. Escribe \'FIN\' para acabar las operaciones y guardar los alumnos registrados.\n")
    nombre_up=nombre.upper()
    if nombre_up!='FIN':
        nota=input("Dame la nota del alumno\n")
        while nota.isalpha():
            nota=input("Debe ser un valor númerico. Dame la nota del alumno\n")
        nota=int(nota)
        notasAlumnos[nombre]=nota

while terminar!=True:
    opciones=input("Escribe 1 para guardar los datos (Si hay datos existentes anteriormente serán borrados), escribe 2 para cargar datos guardados.\n")
    while opciones.isalpha():
        opciones=input("La opcion tiene que ser numerica.\n")
    opciones=int(opciones)
    match opciones:
        case 1:
            with open(ruta, 'wb') as archivo:
                pkl.dump(notasAlumnos,archivo)
                print("Datos guardados correctamente")
                terminar=True
        case 2:
            try:
                with open(ruta, 'rb') as archivo:
                    notasAlumnos=pkl.load(archivo)
                    print("Datos cargados correctamente")
                    for alumno, nota in notasAlumnos.items():
                        print(f"{alumno}:{nota}")
                    terminar=True
            except EOFError:
                print("No hay ningun archivo que cargar.")
                terminar=True
        case _:
            print("No se ha entendido el comando.")