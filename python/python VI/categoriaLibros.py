#Importamos librerias
from tabulate import tabulate

#Definimos variables
libros=[{"Nombre":"Libro 1", "Categoria":"Novela"},{"Nombre":"Libro 2", "Categoria":"Historico"},{"Nombre":"Libro 3", "Categoria":"Manga"},{"Nombre":"Libro 4", "Categoria":"Novela"}]

#Definimos funciones
def libroNovela(lista):
    return lista["Categoria"]=="Novela"

#Logica de programacion
novelas=list(filter(libroNovela, libros))
print(tabulate(novelas, headers="keys", tablefmt="pretty"))