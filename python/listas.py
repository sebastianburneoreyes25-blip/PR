tupla=(1,2,3,4,5) #esto es una tupla
lista=[1,2,3,4,5] #Esto es una lista
print("El contenido de la lista es: \n" ,lista)
print("El contenido de la tupla es: \n", tupla)
lista.append(6)
#tupla.append(6)  <- da error, la lista no tinen metodo append
print(lista)

lista.remove(lista[0])
print(lista)