#Importamos librerias
import numpy as np

#Definimos variables
matriz=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

#Logica de programacion
promMatiz=np.mean(matriz, axis=1)
print(f"Promedio por filas es:{promMatiz}")
