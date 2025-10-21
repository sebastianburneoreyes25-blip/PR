s=int(100)
a=0
while a!=4:
    a=int(input("Ingresa el numero de las siguientes opciones:\n-1.Consultar saldo.\n-2.Ingresar dinero\n-3.Retirar dinero\n-4.Salir\n" ))
    match a:
        case int(1):
            print(f"El saldo disponible es {s}€")
        case int(2):
            b=int(0)
            b=int(input("¿Cuanto dinero vas a ingresar?"))
            s+=b
        case int(3):
            b=int(0)
            b=int(input("¿Cuanto dinero vas a retirar?"))
            if b>s:
                print("Saldo insuficiente.")
            else:
                s-=b
        case int(4):
            print("Cerrando sesion")
        case _:
            print("Opción desconocida. Pruebe de nuevo")
    