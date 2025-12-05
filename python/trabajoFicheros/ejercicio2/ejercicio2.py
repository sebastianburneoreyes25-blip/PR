#Importamos librerias
from pathlib import Path


#Definimos variables
base=Path(__file__).resolve().parent #Esta variable nos dira la ruta donde se este ejecutando el gestor, y .parent cogera solamente el padre, es decir,
                                     #la carpeta donde esté el pograma independientemente del dispositivo o del SO.
ruta=base/"temperaturas.txt"
temperaturasDiarias={"Lunes": 0 ,"Martes": 0 , "Miercoles":0 ,"Jueves":0,"Viernes":0, "Sabado":0, "Domingo":0}

#Logica de programacion
for dia,temperatura in temperaturasDiarias.items():#Recorreremos el diccionario definido para guardar las temperaturas dadas
    correcto=False
    while correcto==False:#Hasta que temperatura no tenga formato adecuado no se pasará a guardar los datos
        temperatura=input(f"Escribe la temperatura del {dia}\n")
        while temperatura.isalpha():
            temperatura=input(f"El formato tiene que ser numerico, acepta decimales. Escribe la temperatura del {dia}\n")
        correcto=True
        temperatura=float(temperatura)
        temperaturasDiarias[dia]=temperatura

with open(ruta, 'w') as archivo:#Guardamos en la ruta especificada los datos.
    for dia,temperatura in temperaturasDiarias.items():
        archivo.write(f"{dia} : {temperatura}\n")