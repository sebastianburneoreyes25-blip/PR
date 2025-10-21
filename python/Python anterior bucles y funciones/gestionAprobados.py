#Entrada del nombre del alumno y crecion de variables a usar
nombre=input("Ingresa el nombre del alumno. Ingresa \"fin\" para terminar y ver cuantos han aprobado\n")
n_l=nombre.lower()
n1=0
n2=0
n3=0
m=0
a=0
s=0

#Pedimos las notas de los examenes
while n_l!="fin":
	n1=float(input("Ingresa la 1 nota\n"))
	n2=float(input("Ingresa la 2 nota\n"))
	n3=float(input("Ingresa la 3 nota\n"))
	m=float((n1+n2+n3)/3)

#Con la media determinamos si ha suspendido o aprobado 
	if m>=float(5):
		a+=1
		print(f"El alumno {nombre} ha aprobado") 
	if m<5:
		s+=1
		print(f"El alumno {nombre} ha suspendido") 
	nombre=input("Ingresa el nombre del alumno. Ingresa \"fin\" para terminar y ver cuantos han aprobado\n")
	n_l=nombre.lower()

#Damos la cantidad de aprobados y suspensos
print(f"Han habido {a} alumnos aprobados y {s} alumnos suspensos")