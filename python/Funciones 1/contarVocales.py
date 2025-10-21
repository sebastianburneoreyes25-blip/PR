#Definimos variables
vocales="aeiou"
palabra=""
numVoc=0


#Definimos funciones
def pedir_palabra():
	a=input("Pon la palabra de la que quieras saber cuantas vocales hay.\n")
	return a

def comparar(cadena,listavocales):
	n=0
	cadenal=cadena.lower()  #Hacemos que la cadena de string sea en minusculas para comparar
	for i in cadenal:
		if i in listavocales:
			n+=1
	return n 



#Logica de programacion

palabra=pedir_palabra()
numVoc=comparar(palabra,vocales)
print(f"En la cadena de letras \"{palabra}\" hay {numVoc} vocales")