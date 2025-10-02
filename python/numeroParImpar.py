#Pedimos el numero a comprobar
a=int(input("Dame el número a comparar\n"))

#Se usa el resto para determinar si es par o impar
b=0
b=a%2

#Expresion de resultados
if b!=0:
	print("El número es impar")
else:
	print("El numero es par")