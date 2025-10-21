#Creamos biblioteca donde se guardara el iventario
inventario={}
cantidad=""

#El usuario empieza a crear el inventario.
producto=input("Añade el producto. Para finalizar, escribe \"fin\"\n")
producto_l=producto.lower()

 #Se seguira creando inventario hasta que el usuario ponga "fin"
while producto_l!="fin":
	if producto_l!="fin":
		if producto in inventario:
			print("El producto esya ya en la lista")
		else:
			cantidad=int(input("Determina la cantidad del producto\n"))
			inventario[producto]=cantidad
	producto=input("Añade el producto. Para finalizar, escribe \"fin\"\n")
	producto_l=producto.lower()

#Imprimimos la biblioteca
for p in inventario.items():
	print(p)

