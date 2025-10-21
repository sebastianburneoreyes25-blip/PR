a=int(input("Dame un numero \n"))

suma= 0 

if a>2:
	suma=suma+1
else:
	suma=suma+2
print("El numero introducido es : ",a, "y el resultado del if es: ",suma)

suma = 0

if (a<2):
	suma=suma+1
	print("a es menor que 2")
elif (a == 2):
	suma=suma+2
	print("a es igual a 2")

else:
	suma = 0
	print("a es mayor que 2")

print(suma)