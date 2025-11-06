#Importamos librerias
import random
import colorama

#Definimos variables
NARANJA = "\033[38;5;208m"

#Definimos funciones
def montruoEleccion(dict,monstruo): #funcion para elegir monstruos
    m=list(dict.keys())
    monstruo=random.choice(m)
    pr=monstruo
    print(NARANJA+ f"{monstruo}"+ colorama.Style.RESET_ALL +" ha aparecido." + colorama.Fore.RED + "¡Preparate para cazarlo!" + colorama.Style.RESET_ALL )
    return monstruo

def nivelDificultad(diff):#Funcion para determinar de manera random el nivel de dificultad de captura
    diff=random.randint(2,6)
    return diff


def difTotal(monstr, presa,diff):#Funcion para definir la resistencia antes de capturarlo al monstruo
    for m,p in monstr.items():
        if presa==m:
            total=p*diff
    return total