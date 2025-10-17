menu={
"Sonic" :( 25.0 , "Plataforma"),
"Mario" :(70, "Plataforma"),
"CoD" :(100 , "Shooter"),
"GTA": (120,"Accion y aventura"),
}
pedido={}
total=0
p=""
print("1-Mostrar productos.\n2-Buscar juego por nombre\n3-Añadir nuevo juego\n4-Precio promedio\n5-Salir")
op=input("Selecciona una opción\n")
while op!="5":
	match  op:
		case "1":
			for a,(b,c) in menu.items():
				print(f"-{a} : {b}€ {c}") 
		case "2":
			producto=input("¿Que juego quieres buscar?\n")
			flag=True
			for a,(b,c) in menu.items():
				al=a.lower()
				producto_l=producto.lower()
				if producto_l==al and flag==True:
					print(f"-{a}  {b}€ {c}")
					flag=False
			if flag==True:
				print("El producto no existe")		
		case "3":
			n=input("¿Como se llama el juego a añadir?")
			p=float(input("¿Cual es el precio del juego?"))
			g=input("¿Que genero es?")
			menu[n]=(p,g)
		case "4" :
			s=0
			for a,(b,c) in menu.items():
				s+=b
			promedio=s/len(menu)
			print(f"El promedio de los juegos es {promedio}€")
		case _:
			print("No entendi el comando. Intentalo de nuevo\n")
	
	print("1-Mostrar productos.\n2-Buscar juego por nombre\n3-Añadir nuevo juego\n4-Precio promedio\n5-Salir")
	op=input("Selecciona una opción\n")
print("Hasta luego!!")