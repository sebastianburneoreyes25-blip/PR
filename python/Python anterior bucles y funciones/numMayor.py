listaNum=[]
hecho=("hecho")
num=0
while num !=hecho:
	listaNum.append(num)
	num=float(num)
	num=input("Introduce el numero. Escribe \" hecho\" para comparar los numeros introducidos. \n")
m=0
n=int(0)
for n in listaNum:
	if int(n) > int(m):
		m=n
	else:
		m=m
print("El numero más alto es ",m )