from pathlib import Path
import pickle as pkl

#Definimos variables
base=Path(__file__).resolve().parent #Esta variable nos dira la ruta donde se este ejecutando el gestor, y .parent cogera solamente el padre, es decir,
                                     #la carpeta donde esté el pograma independientemente del dispositivo o del SO.
ruta=base/"inventario.pkl"
opcionInicial=0


#Defino clases
class Producto:
    def datos(self, nombre, precio, cantidad):
        self.nombre=nombre
        self.precio=precio
        self.cantidad=cantidad
    
#Logica de programación
