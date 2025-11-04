#Definimos variables
listaTareas={}
action=""

#Logica de programacion
print("1.Añadir tarea\n2.Mostrar todas las tareas pendientes\n3.Marcar tarea como completada\n4.Eliminar tarea\n5.Salir")
action=input("Introduce el número de la operacion a realizar.\n")
action=str(action)
while action!="5":
    match action:
        case "1":
            tarea=input("Dime que tarea se realizara\n")
            b="No completada"
            listaTareas[tarea]=b
        case "2":
            for tarea,b in listaTareas.items():
                print(f"-{tarea} {b}")
        case "3":
            compl=input("Dime que tarea quieres completar\n")
            compl_l=compl.lower()
            flag=True
            for tarea,b in listaTareas.items():
                tl=tarea.lower()
                if tl == compl_l:
                    b="Completada"
                    listaTareas[tarea]=b
                    flag=False
            if flag==True:
                print(f"La tarea {compl} no se encuentra en la lista.")
        case "4":
            delete=input("Dime que tarea quieres completar\n")
            del_l=delete.lower()
            flag=True
            d=True
            for tarea,b in listaTareas.items():
                tl=tarea.lower()
                if tl == del_l:
                    d=False
                    flag=False
                    t=tarea
            if flag==True:
                print(f"La tarea {delete} no se encuentra en la lista.")
            elif d==False:
                del listaTareas[t]
        case _: 
            print("No entendi el comando. Prueba de nuevo")
    action=input("Introduce el número de la operacion a realizar.\n")