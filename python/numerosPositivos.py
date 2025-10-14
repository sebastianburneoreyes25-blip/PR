#Entrada de datos y creacion de variables
n=int(input("Dame el numero positivo a sumar. Introduce 0 para finalizar.\n"))
t=0
s=0

#Hasta que el usuario no ponga 0 no se parara de pedir numeros
while n!=0:
	if n>0:
	#Se suma el numero añadido y se suma 1 al contador de numeros totales sumados
		s+=n
		t+=1
	else:
		print("Numero negativo. No se sumará")
	n=int(input("Dame el numero positivo a sumar. Introduce 0 para finalizar.\n"))


#Expresion de datos
print(f"Se han añadido {t} números positivos con un valor de suma {s}")