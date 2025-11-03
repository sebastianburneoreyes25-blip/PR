import fGenerales

def fichaEquipo(lista,clasif):
    n=0
    datos={}
    while n!=5:
        n+=1
        match n:
            case 1:
                id=fGenerales.generaraId(lista)
                datos["ID"]=id
                print(f"Se ha generado un ID {id}")
            case 2:
                nom=input("Escribe el nombre del equipo\n")
                datos["Nombre"]=nom
            case 3:
                cit=input("Escribe la ciudad del equipo\n")
                datos["Ciudad"]=cit
            case 4:
                f=input("Equipo activo:1\nEquipo inactivo:0\n")
                f=fGenerales.activoIncativo(f)
                datos["Activo"]=f
                lista.append(datos)
            case 5:
                dc=datos.copy()
                añadirClas(dc,clasif)


def añadirClas(datos,clasif):
    datos.pop("Ciudad")
    datos.pop("Activo")
    datos["PJ"]=0
    datos["G"]=0
    datos["E"]=0
    datos["P"]=0
    datos["GF"]=0
    datos["GC"]=0
    datos["DG"]=0
    datos["PTS"]=0
    clasif.append(datos)

                

