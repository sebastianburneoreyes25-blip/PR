playlist=[]
pista=""
while pista!="fin":
    pista=input("Agrega el nombre de la canción a añadir a la playlis. Para terminar de añadir escribe en minusculas fin \n")
    if pista!="fin":
        playlist.append(pista)
    else:
        n=0
        for cancion in playlist:
            n=n+1
            print(f"{n}. {cancion}")
m=int(input("Selecciona el numero de la cancion a reproducir. \n"))
print(playlist[(m-1)])
    