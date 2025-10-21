 #Creamos variables y diccionarios a usar.
a=0
l=0
m=0
votos={
"Ana":a,
"Luis":l,
"María":m
}

#DESPLEGAMOS MENU PARA QUE VEA LA LISTA DE CANDIDATOS
print("Lista de candidatos")
for c in votos:
	print(f"-{c}")

#El usuario elige al candidato. Se ira sumando votos hasta que ponga fin. En caso que no exista el candidato, se lo expresa al usuario.
v=input("Pon el nombre de la persona a la que vas a votar. Escribe \"fin\" para finalizar y ver los resultados\n")
v_l=v.lower()
while v_l!="fin":
	match v_l:
		case "ana":
			a+=1
			print("Voto guardado")
			votos["Ana"]=a
		case "luis":
			l+=1
			print("Voto guardado")
			votos["Luis"]=l
		case "maría":
			m+=1
			print("Voto guardado")
			votos["María"]=m
		case _:
			print("No entendi el voto, vuelve a introducirlo")
	v=input("Pon el nombre de la persona a la que vas a votar. Escribe \"fin\" para finalizar y ver los resultados\n")
	v_l=v.lower()

#Desplegamos la cantidad de votos y determinamos ganador.
for i in votos.items():
	print(f"-{i}")
if a>l:
	if a>m:
		print(f"Ana ha sido la más votada con {a} votos")
	elif a<m:
		print(f"María ha sido la más votada con {m} votos")
	else:
		print(f"Empate entre Ana y María")
else:
	if l>m:
		print(f"Luis ha sido el más votado con {l} votos")
	elif l<m:
		print(f"María ha sido la más votada con {m} votos")
	else:
		print(f"Empate entre Luis y María")