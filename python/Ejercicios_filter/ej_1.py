#Definimos variables
numeros = [4, 9, 16, 25, 1, 7, 12]

#Definimos funciones
def mayor10(lista):
    return lista>10

#Logica de programacion
numMayo=list(filter(mayor10,numeros))

print(numMayo)