contacto=""
numero=""
listaContactos={ }
while contacto !="fin":
    contacto=input("Escribe el número del contacto. Escribe en minusculas fin para terminar la agenda\n")
    if contacto!="fin":
        numero=input("Escribe su número telefonico.")
        listaContactos[contacto]=numero
    else:
        n=int(0)
        for nAgenda in listaContactos:
            n=n+1
            print(n, ". ", (nAgenda))
m=input("Selecciona el contacto que quieras ver.\n")
print(listaContactos[m])