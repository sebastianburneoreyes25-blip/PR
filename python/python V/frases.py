#Definimos variables
frases=["la caida del imperio","nacidos de la bruma", "el 13 elemento"]

#Definimos funciones
def frasesATitulo(lista):
    return lista.title()

#Logica de programacion
titulos=list(map(frasesATitulo, frases))
print(titulos)