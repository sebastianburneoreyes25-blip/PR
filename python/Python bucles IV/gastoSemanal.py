gastosSemanal={
    "Lunes" :[],
    "Martes":[],
    "Miercoles":[],
    "Jueves":[],
    "Viernes":[],
    "Sabado":[],
    "Domingo":[]
}
s=0
print("1. Añadir gasto semanal\n2. Mostrar gasto de un día\n3. Ver gasto total semanl\n4. Día con mayor gasto\n5. Salir.")

t=input("Dime que quieres realizar\n")
while t!="5":
    match t:
        case "1":
            d=input("Escribe el día de la semana\n")
            dl=d.lower()
            flag=True
            for a,b in gastosSemanal.items():
                al=a.lower()
                if al==dl:
                    g=float(input("Pon cuanto te has gastado\n"))
                    gastosSemanal[a].append(g)
                    flag=False
            if flag==True:
                print("El día añadido no existe, prueba de nuevo")
        case "2":
            d=input("Escribe el día de la semana\n")
            dl=d.lower()
            flag=False
            for a,b in gastosSemanal.items():
                for a,b in gastosSemanal.items():
                    al=a.lower()
                    if al==dl and flag==False:
                        print(f"-{a}  {b}€")
                        flag=True
        case "3":
                s=s
                for a,b in gastosSemanal.items():
                    x=sum(b)
                    s+=x
                print(f"El gasto semanal es {s}")
        case "4":
            m=0
            for a,b in gastosSemanal.items():
                n=sum(b)
                if m<n:
                    m=n
                    dia=a
            print(f"El dia con mayor gasto es el {dia} con un gasto de {m}€")
        case _:
            print("No entendi el comando, vuelev a intentarlo")

    print("1. Añadir gasto semanal\n2. Mostrar gasto de un día\n3. Ver gasto total semanl\n4. Día con mayor gasto\n5. Salir.")

    t=input("Dime que quieres realizar\n ")