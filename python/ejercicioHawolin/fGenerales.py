#Importamos librerias
import random
import fObjetos
import eso

#Definimos funciones
def ataque(obj,diff,intento,presa):
    if intento>0:
        a=input(f"Escribe con que quieres cazar al monstruo, tienes {intento} oportunidades.\n")
        daño=0
        c=random.randint(3,5)
        al=a.lower()
        for x,y in obj.items():
            xl=x.lower()
            if xl==al:
                daño=y*c
                diff-=daño
        intento-=1
        if diff>0 and intento>0:
            print(f"¡¡oh no!! No hemos conseguido capturar a {presa}\n")
        elif diff>0 and intento<=0:
            print(f"Nos hemos quedado sin intentos.... {presa} ha escapado.....\n")
        elif diff<=0:
            print(f"¡¡{presa} ha sido capturado.... FELICIDADES Y FELIZ JAWOLIN!!  ")
        return diff,intento
            