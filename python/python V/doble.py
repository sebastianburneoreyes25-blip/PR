#Definimos variables
numeros=[0,1,5,8,9,12,45,36,11,7,3,55]

#Definimos funciones
def doble(lista):
    return lista*2

#Logica de programacion
nDobles=list(map(doble, numeros))
print(nDobles)