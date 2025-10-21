#Definimos variables

numeros=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]

pares=0

#Definimos funciones
def contarPar():
	n=0
	for i in numeros:
		if i%2==0:
			n+=1
	return n

def mostrarLista():
	for i in numeros:
		print(i)

#Codigo

mostrarLista()
pares=contarPar()
print(f"Tenemos {pares} numero pares")
