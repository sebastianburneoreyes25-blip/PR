#Importamos librerias
from tabulate import tabulate
import random
import fGenerales
import fMonstruos
import fObjetos

#Definimos variables
monstruos={"Vampiro":10, "Momia":5,"Ghoul":3, "Bruja":8, "Zombie":1}
objetos={"Estaca":5, "Hechizo":8, "Purificacion":10,"Pocion magica":3}
lvlCzador=0
presa=""
dificultad=0

#Logica de programacion

lvlCzador=fGenerales.nivelCazador(lvlCzador)
presa=fMonstruos.montruoEleccion(monstruos,presa)
dificultad=fMonstruos.nivelDificultad(monstruos)
total=fMonstruos.difTotal(monstruos,presa,dificultad)
while total>0:
    fObjetos.mostrarHerramientas(objetos)