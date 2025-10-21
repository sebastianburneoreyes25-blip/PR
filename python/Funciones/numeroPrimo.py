import math  #importarmos libreria de operaciones matematicas

#Definimos variables
num=0
resultado=""

#Definimos funciones
def pedirNum():
	numero=int(input("Escribe el numero entero a comprobar"))
	
	return numero

def comparar(numero):
	primo="es primo"
	for i in range(2, int(math.sqrt(numero))+1):  #Realizamos un bucle for para recorrer del 2 al siguiente nº aproximado de la raiz.
		if numero%i==0:
			primo="no es primo"
	return primo
			
		

#Logica de programacion

num=pedirNum()
resultado=f"El numero {num} " + str(comparar(num))
print(resultado)
