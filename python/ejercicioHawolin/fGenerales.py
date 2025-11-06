#Importamos librerias
import random
import colorama

#Definimos funciones
def ataque(obj,diff,intento,presa):
    if intento>0:
        a=input(f"Escribe con que quieres cazar al monstruo, tienes {intento} oportunidades.\n")
        daño=0
        c=random.randint(3,6)
        al=a.lower()
        flag=False
        for x,y in obj.items():
            xl=x.lower()
            if xl==al:
                daño=y*c
                diff-=daño
                intento-=1
                flag=True
        if flag==True:#Si ha realizado el daño entrara aqui
            if diff>0 and intento>0:
                print(colorama.Fore.LIGHTRED_EX +f"¡¡oh no!! No hemos conseguido capturar a {presa}\n" + colorama.Style.RESET_ALL)
            elif diff>0 and intento<=0:
                print(colorama.Fore.RED+f"Nos hemos quedado sin intentos.... {presa} ha escapado.....\n" +colorama.Style.RESET_ALL)
            elif diff<=0:
                print(colorama.Fore.CYAN+f"¡¡{presa} ha sido capturado.... FELICIDADES Y FELIZ JAWOLIN!!  ")
                calabaza()
        elif flag==False:#Si el objeto no existia entrara aqui
            print("Objeto no esta en la lista, prueba de nuevo")
        return diff,intento

def mostrarHerramientas(obj):#Funcion para imprimir las herramientas a usar
    print("Herramientas para la caza")
    for a,b in obj.items():
        print(f"-{a}")
            
def calabaza():#Funcion para ver una calabaza :)
    NARANJA = "\033[38;5;208m"
    ROJO = colorama.Fore.RED
    VERDE = colorama.Fore.GREEN

    print(VERDE + "          🌿")
    print(NARANJA + "      __________")
    print(NARANJA + "    /           \\")
    print(NARANJA + "   /             \\")
    print(NARANJA + "  |  " + ROJO + "    ◣   ◢" + NARANJA + "    |")
    print(NARANJA + "  |   " + ROJO + "    ▂▂▂" + NARANJA + "     |")
    print(NARANJA + "   \\    \\_____/  /")
    print(NARANJA + "    \\___________/")
    print(colorama.Style.RESET_ALL)