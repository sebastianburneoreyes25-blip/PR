planV=("Madrid", "Barcelona", "Valencia", "Sevilla")
n=0
for ciudad in planV:
	n+=1
	print(f"{n}-{ciudad}")
m=int(input("¿Que ciudad vas a ver?Selecciona el orden de la ciudad\n"))
print(planV[(m-1)])
