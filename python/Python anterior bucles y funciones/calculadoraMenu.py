#Creamos menu visual e imprimimos para que lo vea el usuario
menu=("Sumar","Restar","Multiplicar","Dividir","Salir")
n=0
for a in menu:
	n+=1
	print(f"-{n}.{a}")
#El usuario selecciona la opción a realizar
c=input("Selecciona el numero de la operacion a realizar\n")
a=0
b=0
s=0
r=0
m=0
d=0
#Se compara para realizar una operacion u otra
while c!="5":
	a=int(input("Dame el primer numero\n"))
	b=int(input("Dame el segundo numero\n"))
	match c:
		case "1":
			s=a+b
			print(s)
		case "2":
			r=a-b
			print(r)
		case "3":
			m=a*b
			print(m) 
		case "4":
			d=a/b
			print(d)
		case _:
			print("No entendí. Vuelve a probar")
	c=input("Selecciona el numero de la operacion a realizar.\n")
print("Hasta luego.")