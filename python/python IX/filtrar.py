#Importamos librerias
import numpy as np

#Definimos variables
lista1=[1,8,3,324,222,555,87,1987]
array1=np.array(lista1)

#Logica de programacion
mayores= array1[(array1>35) & (array1<666)]
print(mayores)