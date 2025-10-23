#Defino variables
clases={
    "1DAM":["sebas","taki","desi"],
    "2DAM":["futurosebas", "futurotaki", "futurodesi"],
    "2DAW":["nose"]
}

opcion=""
#Defino funciones

def mostrarMenu():
    print(f"1.Añadir alumno\n2.Mostrar todos los cursos y alumnos\n3.Buscar alumno por nombre\n4.Ver numero total de alumnos.\n5.Salir\n")

def añadir(clases):
    alumno=input("Dime el nombre del alumno a añadir")
    clase=input("Dime la clase a la que ira")
    clasep=clase.upper()
    errclas=True
    for a,b in clases.items():
        if a==clasep:
            clases[a].append(alumno)
        if clasep not in clases and errclas==True:
            print(f"La clase {clase} no existe. Prueba de nuevo")
            errclas=False

        

def cursosAlum(lista):
    for a,b in lista.items():
        print(f"Curso {a}")
        for x in b:
            print(f"-{x}.")

def buscarAlumn(diccionario):
    alumno=input("Dime el nombre del alumno a buscar\n")
    alumnl=alumno.lower()
    
    for a,b in diccionario.items():
        for al in b:
            all=al.lower()
            if all==alumnl:
                print(f"El alumno {alumno} está en la clase {a}")
        
def verNum(dicc):
    ncl={}
    n=0
    nt=0
    for a,b in dicc.items():
        n=len(b)
        ncl[a]=n
        nt+=n
    for x,y in ncl.items():
        print(f"El numero total de la clase {x} es {y} alumnos ")
    print(f"\nEl numero total de alumnos es {nt} ")

#Logica de programacion

while opcion!="5":
    mostrarMenu()
    opcion=input("Dime que operación quieres realizar")
    match opcion:
        case "1":
            añadir(clases)
        case "2":
            cursosAlum(clases)
        case "3":
            buscarAlumn(clases)
        case "4":
            verNum(clases)
        case "5":
            print("Sayonara baby!!")
        case _:
            print("No entendi el comando")
