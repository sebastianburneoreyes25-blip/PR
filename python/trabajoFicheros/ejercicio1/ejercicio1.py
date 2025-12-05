#Importamos librerias
from pathlib import Path


#Definimos variables
base=Path(__file__).resolve().parent #Esta variable nos dira la ruta donde se este ejecutando el gestor, y .parent cogera solamente el padre, es decir,
                                     #la carpeta donde esté el pograma independientemente del dispositivo o del SO.
ruta=base/"nombres.txt"
nombres=[]
nombre=""
nombre_up=""

#Logica de programación 

while nombre_up!="FIN":#Bucle para pedir numeros hasta que se de el comando FIN
    nombre=input("Escribe un nombre. Para acabar de guardar nombres, escribe \'FIN\'.\n")
    nombre_up=nombre.upper()
    if nombre.isalpha():#Comprueba que la variable SOLO tenga letras y no numeros o signos matematicos
        nombres.append(nombre)
    else:
        print("No se admite nada que no sea solo letras.")


with open(ruta, 'w') as archivo:#Abrimos archivo en la ruta previamente creada con Path y añadimos nombre uno por uno.
    for i in nombres:
        archivo.write(f"{i}\n")