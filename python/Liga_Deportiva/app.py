#Importamos librerias
import fGenerales
import fJugadores
import fGestion
import tabulate
import fCalendario

#Definimos variables
equipos=[{"ID":1}, {"ID":2}]
datos={}
jugadores=[]
partidos=[]
elec="0"
listaMenu=[["-1.Gestion de equipos"],["-2.Gestion de jugadores"],["-3.Calendario y partidos"],["-4.Resultados y clasificacion"],["-5.Salir"]]
menuGestion=[["1.Crear equipo"], ["2.Listar equipos"],["3.Buscar por id"],["4.Actualizar datos"], ["5.Eliminar equipo"], ["6.Volver al menu"]]
menuJugadores=[["1.Alta jugador"],["2.Listar jugadores"],["3.Buscar id"],["4.Actualizar"],["5.Eliminar"],["6.Volver a menu"]]
menuCalendarios=[["1.Crear partido"],["2.Listar partidos"], ["3.Reprogramar"], ["4.Eliminar partida"], ["5.Volver a menu"]]

#Logica de programacion
while elec!="5":
    op=0
    fGenerales.mostrarLista(listaMenu)
    elec=input("Selecciona una opción:\n")
    match elec:
        case "1":
            while op!=6:
                p=0
                fGenerales.mostrarLista(menuGestion)
                op=input("Elige una opcion.\n")
                op=fGenerales.esNumerico(op)
                match op:
                    case 1:
                        fGestion.fichaEquipo(equipos)
                    case 2:
                        fGenerales.mostrarListaDic(equipos)
                    case 3:
                        p=fGenerales.bucarId(equipos)
                    case 4:
                        fGenerales.modificar(equipos)
                    case 5:
                        fGenerales.eliminarId(equipos,jugadores,elec)
                    case 6:
                        print("Gusbay")
                    case _:
                        print("No entendi el comando")
        case "2":
            while op!=6:
                p=0
                fGenerales.mostrarLista(menuJugadores)
                op=input("Elige una opcion.\n")
                op=fGenerales.esNumerico(op)
                match op:
                    case 1:
                        fJugadores.fichaJugadores(jugadores,equipos)
                    case 2:
                        fJugadores.mostrarJugadores(jugadores,equipos)
                    case 3:
                        p=fGenerales.bucarId(jugadores)
                    case 4:
                        fGenerales.modificar(jugadores)
                    case 5:
                        fGenerales.eliminarId(jugadores,equipos,elec)
                    case 6:
                        print("Gusbay")
                    case _:
                        print("No entendi el comando")
        case "3":
            while op!=5:
                p=0
                fGenerales.mostrarLista(menuCalendarios)
                op=input("Elige una opcion.\n")
                op=fGenerales.esNumerico(op)
                match op:
                    case 1:
                        fCalendario.fichaPartido(partidos,equipos)
                    case 2:
                        fCalendario.mostrarCalendario(partidos)
                    case 3:
                        fCalendario.modPartido(partidos)
                    case 4:
                       fGenerales.eliminarId(partidos,equipos,elec)
                    case 5:
                       print("Sayonara baby!!")
                    case _:
                        print("No entendi el comando")


        case _:
            print("No entendi ni vergas")

   