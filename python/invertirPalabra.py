#Entrada de datos

palabra=input("Escribe la palabra que quieres invertir\n")
palabra_i=""

#invertimos palabra

for letra in palabra:
	palabra_i=letra+palabra_i

#Expresion de datos

print("El resultado incertido es ", palabra_i)
