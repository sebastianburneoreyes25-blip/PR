productos=[{"Producto":"Manzana", "Tipo":"Fruta"},{"Producto":"Pollo","Tipo":"Carne"},{"Producto":"Chilli en lata","Tipo":"Enlatados"},{"Producto":"Papel higienico","Tipo":"Higiene"}]
perecederos=["Fruta","Carne"]

def filtrarPerecederos(lista):
    
    return lista["Tipo"] in perecederos

productosPerecederos=list(filter(filtrarPerecederos,productos))

print(productosPerecederos)