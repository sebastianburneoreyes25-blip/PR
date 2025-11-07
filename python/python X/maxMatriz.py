#Importamos librerias
import numpy as np

#Definimos variables
matriz=np.random.randint(1,51, size=(4,3))

#Logica de programacion
print(matriz)
max=np.max(matriz, axis=0)
print(f"El maximo por columna es:{max}")