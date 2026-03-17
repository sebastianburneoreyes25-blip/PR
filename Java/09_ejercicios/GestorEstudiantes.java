import java.util.ArrayList;
import java.util.HashMap;

public class GestorEstudiantes {

     /*Desarrolla un programa en Java que permita gestionar un listado de estudiantes desde la terminal.

        El sistema debe permitir que el usuario ingrese tantos estudiantes como desee, por lo que no se conoce de antemano la cantidad de registros. Debido a esto, los estudiantes deben almacenarse utilizando una estructura dinámica y no un arreglo simple.

        Cada estudiante tendrá la siguiente información:

        * Nombre
        * Edad
        * Nota final

        El programa debe mostrar un menú interactivo que se repita hasta que el usuario decida salir.



        Funcionalidades del sistema

        El menú debe permitir las siguientes opciones:

        1.- Agregar estudiante
        El usuario debe poder ingresar los datos de un estudiante:
        nombre
        edad
        nota final

        El estudiante se debe guardar en la lista.

        2.- Mostrar todos los estudiantes
        El programa debe mostrar todos los estudiantes almacenados en la lista.
        Si no hay estudiantes registrados, el programa debe mostrar un mensaje indicando que no hay estudiantes en el sistema.

        3.- Modificar estudiante
        El usuario debe ingresar el nombre del estudiante que desea modificar.
        Si el estudiante existe, el programa debe permitir cambiar:
        * edad
        * nota final

        Si el estudiante no existe, el programa debe mostrar un mensaje indicando que no se encontró el estudiante.

        4.- Eliminar estudiante
        El usuario debe ingresar el nombre del estudiante que desea eliminar.
        Si el estudiante existe, se elimina de la lista.
        Si no existe, el sistema debe mostrar un mensaje indicando que no se encontró el estudiante.

        5.- Eliminar todo el listado
        El sistema debe permitir eliminar todos los estudiantes almacenados, dejando la lista vacía.

        6.- Mostrar estudiantes aprobados
        El programa debe mostrar únicamente los estudiantes cuya nota sea mayor o igual a 5.

        7.- Salir
        Valida si el Usuario, ¿Está seguro que desea salir s/n?
        Finaliza la ejecución del programa. */
    public static void main(String[] args) {
       
        String[] menu={"1.Agregar estudiante.","2.Mostrar todos los estudiantes","3.Modificar estudiante","4.Eliminar estudiante",
        "5.Eliminar todo el listado","6.Mostrar estudiantes","7.Salir"};
        
        ArrayList<HashMap<String, float[]>> estudiantes=new ArrayList<>();//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA



    }

}
