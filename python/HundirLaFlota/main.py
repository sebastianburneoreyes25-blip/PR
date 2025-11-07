#Importamos librerias
import numpy as np
import fBarcos


#Definimos variables
tableroUser=np.zeros((20,20))
tableroBarcos=np.zeros((20,20))
intentos=0
barco1=np.array([1,1])
barco2=np.array([1,1,1])
barco3=np.array([1,1,1,1])

#Logica de programacion
fBarcos.esconderBarco(barco1, tableroBarcos)
fBarcos.esconderBarco(barco3, tableroBarcos)
fBarcos.esconderBarco(barco2, tableroBarcos)
print(len(barco3))
print(tableroBarcos)

