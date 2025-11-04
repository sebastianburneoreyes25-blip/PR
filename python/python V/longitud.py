#Definimos variables
palabra=["imperio","nacidos ", "elemento","radiante"]

#Definimos funciones
def calcularLongitud(lista):
    return len(lista)

#Logica de programacion
longitud=list(map(calcularLongitud,palabra))
print(longitud)