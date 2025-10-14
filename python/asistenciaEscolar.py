#Definimos el diccionario asistencia, asi como el contador de si y no.
asistencia={
"Lunes":"s/n",
"Martes":"s/n",
"Miercoles":"s/n",
"Jueves":"s/n",
"Viernes":"s/n"
}
s=0
n=0

#El usuario pondra los días que ha asistido el alumno
for a in asistencia:
	b=input(f"Ha asistido el {a} el alumno. \"S\"para sí, \"N\"para no.\n")
	b_l=b.lower()
	if b_l=="s":
		s+=1
	elif b_l=="n":
		n+=1
	asistencia[a]=b

#Imprimimos el diccionario y mostramos el porcentaje de asistencia
for a in asistencia.items():
	print(f"-{a}")
p=0
p=(s/5)*100
print(f"El alumno ha asistido {s} días, faltado {n}días.\nPorcentaje de asistencia:{p}%")