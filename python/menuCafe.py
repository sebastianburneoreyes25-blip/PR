#Creamos el menu
menu={
	'Café':(1.75 , 40),
	'Té':(1.75 , 20),
	'Tostada con tomate':(2.5 , 120),
	'Bocadillo panceta':(3.0 , 220)
}

#Imprimimos el menu
i='Café'
a,b=i
for i in menu:
	a,b=i
	print(f"-{i}: {a}€ {b}Cal")

#El usuario elije algo del menu, si escribre algo que no este en el, le volvera a pedir introducir los datos.
selec=input("Añade productos del menú, para finalizar escribe fin.\n")
selec_l=selec.lower()
calorias=0
precio=0
pedido=[]
while selec_l!="fin":
	if selec in menu:
		#Sumamos precio y calorias
		for i,(b,c) in menu.items():
			if i == selec:
				precio+=float(b)	
				calorias+=c
				pedido.append(i)
		selec=input("Añade productos del menú, para finalizar escribe fin.\n")
		selec_l=selec.lower()
	else:
		print(f"{selec} no est en el menu, elige una de las opciones dadas.")
		selec=input()
#Salida de datos.
for p in pedido:
	print(f"-{p}\n")
print(f"Total a pagar:{precio}€\nCalorias totales:{calorias}Cal")
	
	