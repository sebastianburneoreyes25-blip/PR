#Importamos la funcion random
import random

#Seleccionamos con la funcion randint un numero entre el 1 y 100
a=random.randint(1,100)

#Pedimos el numero que cree que es y expresamos si es bajo, alto o adivino el número.

b=int(input("Pon el numero que crees que es\n"))

if b<a:
	print("Demasiado bajo")
elif b==a:
	print ("OLEEEEEEEEEEE ese eraaaaa")
else:
	print ("Demasiado alto")