#Definimos variables

lim=0
suma=0

#Definimos funciones

def suma_hasta_limite(numerolimite):
	n=0
	for i in range(numerolimite+1):
		n+=i
	return n	




def limite():
	a=int(input("Define el limite con numero entero.\n"))
	return a


#Logica
lim=limite()
suma=suma_hasta_limite(lim)
print(f"El resultado del sumatorio hasta {lim} es {suma}")