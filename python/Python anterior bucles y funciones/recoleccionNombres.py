listaNombres=[]
n=input("Introduce el nombre a guardar. Escribre fin para finalizar ")

while n!="fin":
	listaNombres.append(n)
	n=input("Introduce el nombre a guardar. Escribre fin para finalizar ")
print(listaNombres)
for nombre in listaNombres:
	print(nombre)
