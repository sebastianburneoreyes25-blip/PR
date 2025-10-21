inventario={
"Leche":(0.75, 500),
"Pan":(0.70, 300),
"Jamon York":(2.5, 200),
"Queso":(3,250),
}

valor_total=""
producto_requerido=""

def menu():
	print("1.Mostrar inventario\2.Vender producto\n3.Añadir producto\n4.Calcular valor total del stock\n5.Salir")

def calcularStock():
	for p,(pr,s) in inventario.items:
		stock_valor+=pr*s
	return stock_valor


def mostarmenu():
	for p,(pr,s) in inventario.items():
		print(f"-{p} {pr}€ {s}Uds")

def  vender(producto):
	producto=input("Dime que producto venderas")
	for p in inventario.items():
		if p==producto:
			s-=1
			p=pr,s

def añadirProducto():

	
			