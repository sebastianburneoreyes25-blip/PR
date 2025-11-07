#Importamos librerias
import numpy as np

#Definimos variables

#Logica de programacion
matriz=np.arange(1,17)
matriz=matriz.reshape(4,4)
print(matriz)
columna3=matriz[:,2]
print(f"La comulna 3 es :\n{columna3}")