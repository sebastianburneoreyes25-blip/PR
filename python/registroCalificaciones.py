#Creamos variables a definir
calificaciones={}
clase=""
clase_l=clase.lower()
nota=0
promedio=0
n=0

#Empezamos el bucle hasta que el usuario ponga fin
while clase_l!="fin":
	clase=input("Escribe el nombre de la clase\n")
	clase_l=clase.lower()
	if clase_l!="fin":
		nota=float(input("Escribe la clasificacion que sacaste en numeros"))
		promedio+=nota
		calificaciones[clase]=nota
		n+=1

#Imprimimos con un for la clave asignatura y su valor
for c , m in calificaciones.items():
	print(f"-{c}:{m}")	

#Hacemos la media
promedio=promedio/n
print(f"La nota media es:\n{promedio}")