def esNumerico(a):
    while a.isalpha():
        a=input("Tiene que ser un numero")
    a=float(a)
    return a

altura=input("Dame la altura del rectangulo en cm\n")
altura=esNumerico(altura)
base=input("Dame la base del rectangulo en cm\n")
base=esNumerico(base)

area=base*altura

print(f"El area es {area} cm2")
