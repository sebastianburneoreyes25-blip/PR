import random
import colorama

NARANJA = "\033[38;5;208m"

def montruoEleccion(dict,monstruo):
    m=list(dict.keys())
    monstruo=random.choice(m)
    pr=monstruo
    print(NARANJA+ f"{monstruo}"+ colorama.Style.RESET_ALL +" ha aparecido." + colorama.Fore.RED + "¡Preparate para cazarlo!" + colorama.Style.RESET_ALL )
    return monstruo

def nivelDificultad(diff):
    diff=random.randint(2,6)
    return diff


def difTotal(monstr, presa,diff):
    for m,p in monstr.items():
        if presa==m:
            total=p*diff
    return total