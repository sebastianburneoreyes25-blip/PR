#Definimsos variables
alturas_metros = [1.60, 1.75, 1.80, 1.50]

#Definimos funciones
def metroCentimetro(lista):
    return lista*100

#Logica de programacion
alturasCentimetro=list(map(metroCentimetro,alturas_metros))

print(alturasCentimetro)