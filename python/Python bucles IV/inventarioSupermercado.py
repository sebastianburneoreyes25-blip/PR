#Definimos variables

inventario={
"Leche":(0.75, 500),
"Pan":(0.70, 300),
"Jamon York":(2.5, 200),
"Queso":(3,250),
}
eleccion=""
valor_total=""
producto_requerido=""

#Definimos funciones
def menuEleccion():
	print("1.Mostrar inventario\n2.Vender producto\n3.Añadir producto\n4.Calcular valor total del stock\n5.Salir")
	a=input("Escoge\n")

	return a

def calcularStock():
	stock_valor=0
	for p,(pr,s) in inventario.items():
		stock_valor+=(pr*s)
	return stock_valor


def mostarmenu():
	for p,(pr,s) in inventario.items():
		print(f"-{p} {pr}€ {s}Uds")

def  vender(producto,inventario):
	producto=input("Dime que producto venderas\n")
	for p,(pr,s) in inventario.items():
		pl=p.lower()
		if pl==producto:
			s-=1
			pr=pr
			p=p
			return p,pr,s

def añadirProducto():
	p=input("Dime el nombre del producto a añadir:\n")
	pr=float(input("Dime cuanto cuesta: \n"))
	s=int(input("Cuantos productos necesitas añadir\n"))

	return p,pr,s

#Logica de programacion
while eleccion!="5":
	eleccion=menuEleccion()
	match eleccion:
		case "1":
			mostarmenu()

		case "2":
			p,pr,s=vender(producto_requerido, inventario)
			inventario[p]=pr,s
			mostarmenu()
		case "3":
			p,pr,s=añadirProducto()
			inventario[p]=pr,s
			mostarmenu()

		case "4":
			valor_total= calcularStock()
			print(f"{valor_total}€")

		case "5":
			print("Sayonara baby!!")
		case _:
			print("No entendi el comando")