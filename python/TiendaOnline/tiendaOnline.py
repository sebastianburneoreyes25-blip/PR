#Importamos lisbrerias
import funciones_tienda
import funciones_ventas


#Definimos variables
menuOpciones=["\nElige el menu:","-1.Articulos","-2.Usuario","-3.Ventas/Carrito","-4.Salir"]
menuUsuario=["\n1.Crear usuario","2.Listar usuario","3.Buscar usuario por id.","4.Actualizar usuario","5.Eliminar usuario","6.Alternar activo/inactivo","7.Salir"]
menuArticulos=["\n1.Crear articulo","2.Listar articulos","3.Buscar articulo por id.","4.Actualizar articulo","5.Eliminar articulo","6.Alternar activo/inactivo","7.Salir"]
menuVentas=["VENTAS / CARRITO\n","1.Seleccionar usuario activo","2.Añadir articulo al carrito","3.Quitar articulos del carrito","4.Ver carito (detalles y total)","5.Confirmar compra","6.Historial de ventas por usuario","7.Vaciar carrito","8.Salir"]
producto={
}
listaArticulos=[
]
user={
}
listaUsuarios=[
]
carrito=[
]
registroVentas={
}
usuarioActivo=[
]
eleccion=""
tipo=""
n=False
idCarro=0


#Logica de programacion
while tipo!="4":
    tipo=""
    eleccion=""
    funciones_tienda.menu(menuOpciones)
    tipo=str(input("Elige el tipo de operacion.\n"))
    match tipo:
        case "1":
            while eleccion!="7":
                funciones_tienda.menu(menuArticulos)
                eleccion=input("Elige una operacion.\n")
                match eleccion:
                    case "1":
                        funciones_tienda.crear(producto,listaArticulos,tipo)
                    case "2":
                        funciones_tienda.mostrarLista(listaArticulos,tipo,eleccion)
                    case "3":
                        funciones_tienda.buscarPorId(listaArticulos)
                    case "4":
                        funciones_tienda.actualizar(listaArticulos,tipo)####Nota para mi: modificar para no poder cambiar id nunca
                    case "5":
                        funciones_tienda.eliminar(listaArticulos)
                    case "6":
                        funciones_tienda.alernarStatus(listaArticulos)
                    case "7":
                        print("Sayonara baby!!")
                    case _:
                        print("No entendi el comando. Prueba de nuevo")
        case "2":
            while eleccion!="7":
                funciones_tienda.menu(menuUsuario)
                eleccion=input("Elige una operacion.\n")
                match eleccion:
                    case "1":
                        funciones_tienda.crear(user,listaUsuarios,tipo)
                    case "2":
                        funciones_tienda.mostrarLista(listaUsuarios,tipo,eleccion)
                    case "3":
                        funciones_tienda.buscarPorId(listaUsuarios)
                    case "4":
                        funciones_tienda.actualizar(listaUsuarios,tipo)
                    case "5":
                        funciones_tienda.eliminar(listaUsuarios)
                    case "6":
                        funciones_tienda.alernarStatus(listaUsuarios)
                    case "7":
                        print("Sayonara baby!!")
                    case _:
                        print("No entendi el comando. Prueba de nuevo")
        case "3":
            while eleccion!="8":
                funciones_tienda.menu(menuVentas)
                eleccion=input("Elige una operacion.\n")
                match eleccion:
                    case "1":
                        usuarioActivo.append(funciones_ventas.select(usuarioActivo,listaUsuarios,eleccion))
                        if len(usuarioActivo)>0:
                            n=True
                        else:
                            n=False
                    case "2":
                        if n==True:
                            producto=funciones_ventas.select(carrito, listaArticulos,eleccion)
                            if len(producto)>0:
                                carrito.append(producto)
                        if n==False:
                            print("Se necesita tener un usuario seleccionado para agregar productos.")
                    case "3":
                        if len(carrito)>0:
                            funciones_tienda.eliminar(carrito)
                        else:
                            print("No hay articulos para eliminar")
                    case "4":
                        funciones_tienda.mostrarLista(carrito,tipo,eleccion)
                    case "5":
                       funciones_ventas.confirmarCompra(carrito,usuarioActivo,registroVentas,listaArticulos)
                    case "6":
                        funciones_tienda.mostrarLista(registroVentas,tipo,eleccion)
                    case "7":
                        funciones_ventas.vaciar(carrito)
                    case "8":
                        print("Sayonara baby!")
                    case _:
                        print("No entendi el comando. Prueba de nuevo")
        case "4":
            print("Hasta la vista ganster")
        case _:
            print("No entendi el comando, prueba de nuevo")