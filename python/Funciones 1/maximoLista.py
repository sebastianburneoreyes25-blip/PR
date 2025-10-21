#Definimos variables
numeros=[1,2,3,4,5,6,7,87,99,10,11,12,13,14]

max=0


#Definimos funciones

def imprimirLista():
	for i in numeros:
		print(i)

def comparar():
	n=0
	for i in numeros:	
		if i>n:
			n=i

	return n

#Logica de programacion
imprimirLista()
max=comparar()
print(f"El numero maximo es: {max}")