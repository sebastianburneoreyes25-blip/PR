listaTareas={}
action=""
print("1.Añadir tarea\n2.Mostrar todas las tareas pendientes\n3.Marcar tarea como completada\n4.Eliminar tarea\n5.Salir")
action=input("Introduce el número de la operacion a realizar.\n")
action=str(action)
while action!="5":
    match action:
        case "1":
            tarea=input("Dime que tarea se realizara")
            b="No completada"
            listaTareas[tarea]=b
        case "2":
            for tarea,b in listaTareas.items():
                print(f"-{tarea} {b}")
        case "3":

        case "4":
            
        case _: 
            print("No entendi el comando. Prueba de nuevo PUTON")
    action=input("Introduce el número de la operacion a realizar.\n")