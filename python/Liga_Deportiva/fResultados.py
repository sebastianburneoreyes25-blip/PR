import fGenerales



def registrarResultados(listaCal,clasif):#Funcion para registrar los resultados de un partido
    l=[]
    for i in listaCal:
        if i["Jugado"]==False:
            l.append(i)
    fGenerales.desplegarDic(l)
    selec=input("Escribe el id del partido que quieras registrar sus resultados")
    selec=fGenerales.esNumerico(selec)
    for i in listaCal:
        if selec==i["ID"]:
            gl=input("¿Cuantos goles ha marcado el equipo local?")
            gl=fGenerales.esNumerico(gl)
            gv=input("¿Cuantos goles ha marcado el equipo local?")
            gv=fGenerales.esNumerico(gv)
            i["Resultado"]=({"Goles local": gl, "Goles visitante":gv})
            i["Jugado"]=True
            actualizarClas(i,clasif)




def actualizarClas(partido,clasif):#Funcion para actualizar la lista de la clasificacion
    for j in clasif:
        if j["ID"]==partido["ID Local"]:
            j["PJ"]+=1
            result=partido["Resultado"].copy()
            j["GF"]+=result["Goles local"]
            j["GC"]+=result["Goles visitante"]
            j["DF"]=j["GF"]-j["GC"]
            if result["Goles local"]<result["Goles visitante"]:
                j["P"]+=1
            elif result["Goles local"]>result["Goles visitante"]:
                j["G"]+=1
            elif result["Goles local"]==result["Goles visitante"]:
                j["E"]+=1
            j["PTS"]=(j["G"]*3)+j["E"]
        elif j["ID"]==partido["ID Visitante"]:
            j["PJ"]+=1
            result=partido["Resultado"].copy()
            j["GF"]+=result["Goles visitante"]
            j["GC"]+=result["Goles local"]
            j["DF"]=j["GF"]-j["GC"]
            if result["Goles local"]<result["Goles visitante"]:
                j["G"]+=1
            elif result["Goles local"]>result["Goles visitante"]:
                j["P"]+=1
            elif result["Goles local"]==result["Goles visitante"]:
                j["E"]+=1
            j["PTS"]=(j["G"]*3)+j["E"]



def ordClasif(clasif):#Funcion para ordenar la clasificacion de los equipos.
    listaOrdenada=sorted(clasif, key=lambda x: x['PTS'], reverse=True)
    fGenerales.desplegarDic(listaOrdenada)

def statsSimple(clasif):
    p=["ID","Nombre","PJ","PTS","DF"]
    id=input("Escribe el id del equipo")
    id=fGenerales.esNumerico(id)
    cl={}
    for i in clasif:
        if i["ID"]==id:
           for a,b in i.items():
               if a in p:
                   cl[a]=b
    f=[cl]

    fGenerales.desplegarDic(f)


