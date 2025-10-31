import fGenerales

def fichaEquipo(lista):
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
                nom=input("Escribe el nombre del equipo")
                datos["Nombre"]=nom
            case 3:
                cit=input("Escribe la ciudad del equipo")
                datos["Ciudad"]=cit
            case 4:
                f=input("Equipo activo:1\nEquipo inactivo:0\n")
                f=fGenerales.activoIncativo(f)
                datos["Activo"]=f
                lista.append(datos)


                
                






    



                
                




