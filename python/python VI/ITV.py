#Definimos variables
coches=[{"Matricula":"0544KLM", "ITV":"Aprobada"}, {"Matricula":"1564ASD", "ITV":"Desfavorable"}, {"Matricula":"9987KKK", "ITV":"Aprobada"}, {"Matricula":"5698LOP", "ITV":"Desfavorable"}]

#Definimos funciones
def itvAprobada(lista):
    return lista["ITV"]=="Aprobada"

#Logica de programacion
cochesAprobados=list(filter(itvAprobada, coches))
print(cochesAprobados)