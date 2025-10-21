a=int(input("Dame un numero entero para el promedio. Para finalizar el promdio introduce el 0. \n"))

suma=0
promedio=0
contador=0
while a!= 0:
	suma+=a
	contador+=1
	a=int(input("Dame un numero entero para el promedio. Para finalizar el promdio introduce el 0. \n"))

promedio=suma/contador
print("El promedio es ",promedio)	