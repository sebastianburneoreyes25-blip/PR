playlist=[]
pista=""
pista_l=pista.lower()
while pista_l!="fin":
	pista=input("Agrega el nombre de la canción a añadir a la playlis. Para terminar de añadir escribe en minusculas fin \n")
	pista_l=pista.lower()
	if pista_l!="fin":
		playlist.append(pista)
n=0
for cancion in playlist:
	n=n+1
	print(n, ". ", (cancion))
m=int(input("Selecciona el numero de la cancion a reproducir. "))
print(playlist[(m-1)])
    