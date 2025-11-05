import random


def montruoEleccion(dict,monstruo):
    m=list(dict.keys())
    monstruo=random.choice(m)
    pr=monstruo
    print(f"{monstruo} ha aparecido. ¡Preparate para cazarlo!")
    return monstruo

def nivelDificultad(diff):
    diff=random.randint(2,6)
    print(diff)
    return diff


def difTotal(monstr, presa,diff):
    for m,p in monstr.items():
        if presa==m:
            total=p*diff
    print(total)
    return total