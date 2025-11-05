#Importamos librerias
from tabulate import tabulate
import random
import fGenerales
import fMonstruos
import fObjetos

#Definimos variables
monstruos={"Vampiro":20, "Momia":11,"Ghoul":3, "Bruja":18, "Zombie":1}
objetos={"Estaca":1, "Hechizo":5, "Purificacion":5,"Pocion magica":3}
presa=""
dificultad=0
intentos=3

#Logica de programacion
presa=fMonstruos.montruoEleccion(monstruos,presa)
dificultad=fMonstruos.nivelDificultad(monstruos)
total=fMonstruos.difTotal(monstruos,presa,dificultad)
while total>0:
    fObjetos.mostrarHerramientas(objetos)
    total,intentos=fGenerales.ataque(objetos,total,intentos,presa)
