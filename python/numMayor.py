listaNum=[]
hecho=("hecho")
num=0
while num !=hecho:
	num=input("Introduce el numero. Escribe \" hecho\" para comparar los numeros introducidos. \n")
	if num!=hecho:
		num=float(num)
		listaNum.append(num)
m=0
for n in listaNum:
	if float(n) > float(m):
		m=n
print("El numero más alto es ",m )