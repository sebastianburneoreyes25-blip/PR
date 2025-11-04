#Defino variables
productos=[{"Producto":"Manzana", "Tipo":"Fruta"},{"Producto":"Pollo","Tipo":"Carne"},{"Producto":"Chilli en lata","Tipo":"Enlatados"},{"Producto":"Papel higienico","Tipo":"Higiene"}]
perecederos=["Fruta","Carne"]

#Definimos funciones
def filtrarPerecederos(lista):
    
    return lista["Tipo"] in perecederos

#Logica de programacion
productosPerecederos=list(filter(filtrarPerecederos,productos))

print(productosPerecederos)