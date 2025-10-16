menu={
"Papel" :( 5.0 , 800),
"Bolis" :(0.85, 75),
"Lapiz" :(0.5 , 100),
"Sacapuntas": (0.75,75),
"Borrador": (0.25, 100),
"Cuaderno":(1.00, 75)
}
pedido=[]
total=0
p=""
print("1-Mostrar productos.\n2-Añadir producto al carrito\n3-Ver total compra\n4-Salir")
op=input("Selecciona una opción")
while op!="4":
	match  op:
		case "1":
			for a,(b,c) in menu.items():
				print(f"-{a} : {b}€ {c} Unidades") 
		case "2":
			producto=input("Añade el nombre del articulo a añadir al pedido")
			for a,(b,c) in menu.items():
				if producto==a:
					pedido.append(a)
					total+=b
					c-=1
		case "3":
			print(f"El total es {total}€")
		case _ :
			print("No entendi el comando. Vuelve a introducirlo")
	print("\n1-Mostrar productos.\n2-Añadir producto al carrito\n3-Ver total compra\n4-Salir")
	op=input("Selecciona una opción")