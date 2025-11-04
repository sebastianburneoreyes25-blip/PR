#Definimos variables
numeros=[0.15,1.8,18.3,5.5,3.3,3.7]

#Definimos funciones
def redondear(lista):
    return round(lista)

#Logica de programacion
redondeo=list(map(redondear,numeros))
print(redondeo)