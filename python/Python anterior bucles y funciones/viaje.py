#Creamos la tupla
planV=("Madrid", "Barcelona", "Valencia", "Sevilla")
n=0

#Imprimimos con buvle for los items de la tupla
for ciudad in planV:
	n+=1
	print(f"{n}-{ciudad}")

#El usuario puede visualizar con el numero la ciudad que se visitará
m=int(input("¿Que ciudad vas a ver?Selecciona el orden de la ciudad\n"))
print(planV[(m-1)])
