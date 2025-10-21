#Pedimos los numeros y la operación que quieren realizar

a=int(input("Dame el primer número \n"))

b=int(input("Dame el segundo número \n"))

c=input("¿Quieres sumar, restar, multiplicar o dividir? \nEscribe el comando en minusculas\n")

#Definimos las variables de la operación
s=0
r=0
m=0
d=0

#Se comprueba el comando y se ejecutra segun lo introducido.
match c:
	case "sumar":
		s=a+b
		print("El resultado es: ", s)

	case "restar":
		r=a-b
		print("El resultado es: ", r)
	case "multiplicar":
		m=a*b
		print("El resultado es: ", m)
	case "dividir":
		d=a/b
		print("El resultado es: ", d)
	case _:
		print("No entendí el comando. Prueba de nuevo")