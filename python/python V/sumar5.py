#Definimos variables
numeros=[0,1,5,8,9,12,45,36,11,7,3,55]

#Definimos funciones
def masCinco(lista):
    return lista+5

#Logica de programacion
numerosCinco=list(map(masCinco, numeros))
print(numerosCinco)