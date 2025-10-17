notas={
    "PR" :[],
    "HC":[],
    "SI":[],
    "ED":[],
    "BBDD":[],
    "LM":[],
}
print("1-Añadir nota a la asignatura.\n2-Ver notas de la asignatura.\n3-Calcular media por asignatura\n4-Promedio\n5-Salir")
t=input("Dime que quieres realizar\n")
while t!="5":
    match t:
        case "1":
            asig=input("Escribe el nombre de la asignaruta\n")
            asig_l=asig.lower()
            flag=True
            for a,b in notas.items():
                al=a.lower()
                if al==asig_l:
                    puntuacion=float(input("Pon cuanto has sacado\n"))
                    notas[a].append(puntuacion)
                    flag=False
            if flag==True:
                print("El día añadido no existe, prueba de nuevo")
        case "2":
            asig=input("Escribe el nombre de la asignaruta\n")
            asig_l=asig.lower()
            flag=True
            for a,b in notas.items():
                al=a.lower()
                if al==asig_l:
                    for puntuaje in b:
                        print(f"-{puntuaje}")
        case "3":
            asig=input("Escribe el nombre de la asignaruta\n")
            asig_l=asig.lower()
            flag=True
            mediaAsignatura=0
            for a,b in notas.items():
                al=a.lower()
                if al==asig_l:
                    mediaAsignatura=sum(b)/len(b)
                    print(f"La media de la asignatura {a} es {mediaAsignatura}")
        case "4":
            m=0
            mg=0
            for a, b in notas.items():
                m=sum(b)/len(notas)
                mg+=m
            print(f"La media general es {mg}")
        case _:
            print("Comando erroneo. Prueba de nuevo")
    print("1-Añadir nota a la asignatura.\n2-Ver notas de la asignatura.\n3-Calcular media por asignatura\n4-Promedio\n5-Salir")
    t=input("Dime que quieres realizar\n")