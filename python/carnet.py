#Realizaremos un programa que pida al usuario la edad.

#Si la edad del usuario está entre los 18 y los 80, el sistema mostrará un mensaje diciendo: "puedes tener el carnet de conducir"

#Si la edad del usuario es superior a los 80 años el sistema mostrará un mensaje diciendo: "Es hora de que tus hijos te hagan de chofer"

#vamos a ir pidiendo la edad de manera cronologicajmn

edad=int(input("Escribe tu edad \n"))

if (edad>=18) and (edad <80):
	print("puedes tener el carnet de conducir")
elif (edad >=80):
	print ("Es hora de que tus hijos te hagan de chofer")
elif (edad <=0):
	print("Todavia ni naces")
else:
	print("Todavia eres menor, no tienes carnet")
