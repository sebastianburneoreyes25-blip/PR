#Importamos librerias
from pathlib import Path#Importamos path para tener las rutas de archivos concretos. En nuestro caso para tener la ruta de donde se esté ejecutando el programa
import gestorCore as gc

#Definimos variables
listaClientes=[]
base=Path(__file__).resolve().parent #Esta variable nos dira la ruta donde se este ejecutando el gestor, y .parent cogera solamente el padre, es decir,
                                     #la carpeta donde esté el pograma independientemente del dispositivo o del SO.
ruta=base/"clientes.pkl"
menu=["1.Alta cliente","2.Listar clientes","3.Buscar cliente por DNI","4.Modificar télefono del cliente","5.Eliminar cliente","6.Guardar clientes en fichero","7.Cargar clientes en fichero","8.Salir"]
elec=0
funcion=0

#Logica de programacion
print("Bienvenido al gestor de clientes. A continuacion veras las opciones del gestor.")
while elec!=8:
    gc.mostrarMenu(menu)
    elec=gc.esNumerico(input("¿Que operacion quieres hacer?\n"))
    match elec:
        case 1:
            gc.altaCliente(listaClientes)
        case 2:
            gc.listarClientes(listaClientes)
        case 3:
            funcion=0
            gc.buscarDNI(listaClientes,funcion)
        case 4:
            gc.modificarTelefono(listaClientes)
        case 5:
            gc.eliminarCliente(listaClientes)
        case 6:
            gc.guardarListaClientes(listaClientes,ruta)
        case 7:
            listaClientes.append(gc.cargarLista(ruta))
        case 8:
            print("Hasta luego")
        case _:
            print("No entendí el comando. Prueba de nuevo")