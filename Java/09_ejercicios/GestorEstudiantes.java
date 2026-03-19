import java.util.ArrayList;
import java.util.Scanner;

public class GestorEstudiantes {

    /*
     * Desarrolla un programa en Java que permita gestionar un listado de
     * estudiantes desde la terminal.
     * 
     * El sistema debe permitir que el usuario ingrese tantos estudiantes como
     * desee, por lo que no se conoce de antemano la cantidad de registros. Debido a
     * esto, los estudiantes deben almacenarse utilizando una estructura dinámica y
     * no un arreglo simple.
     * 
     * Cada estudiante tendrá la siguiente información:
     * 
     * Nombre
     * Edad
     * Nota final
     * 
     * El programa debe mostrar un menú interactivo que se repita hasta que el
     * usuario decida salir.
     * 
     * 
     * 
     * Funcionalidades del sistema
     * 
     * El menú debe permitir las siguientes opciones:
     * 
     * 1.- Agregar estudiante
     * El usuario debe poder ingresar los datos de un estudiante:
     * nombre
     * edad
     * nota final
     * 
     * El estudiante se debe guardar en la lista.
     * 
     * 2.- Mostrar todos los estudiantes
     * El programa debe mostrar todos los estudiantes almacenados en la lista.
     * Si no hay estudiantes registrados, el programa debe mostrar un mensaje
     * indicando que no hay estudiantes en el sistema.
     * 
     * 3.- Modificar estudiante
     * El usuario debe ingresar el nombre del estudiante que desea modificar.
     * Si el estudiante existe, el programa debe permitir cambiar:
     * edad
     * nota final
     * 
     * Si el estudiante no existe, el programa debe mostrar un mensaje indicando que
     * no se encontró el estudiante.
     * 
     * 4.- Eliminar estudiante
     * El usuario debe ingresar el nombre del estudiante que desea eliminar.
     * Si el estudiante existe, se elimina de la lista.
     * Si no existe, el sistema debe mostrar un mensaje indicando que no se encontró
     * el estudiante.
     * 
     * 5.- Eliminar todo el listado
     * El sistema debe permitir eliminar todos los estudiantes almacenados, dejando
     * la lista vacía.
     * 
     * 6.- Mostrar estudiantes aprobados
     * El programa debe mostrar únicamente los estudiantes cuya nota sea mayor o
     * igual a 5.
     * 
     * 7.- Salir
     * Valida si el Usuario, ¿Está seguro que desea salir s/n?
     * Finaliza la ejecución del programa.
     */
    public static void main(String[] args) {

        String[] menu = { "1.Agregar estudiante.", "2.Mostrar todos los estudiantes", "3.Modificar estudiante",
                "4.Eliminar estudiante",
                "5.Eliminar todo el listado", "6.Mostrar estudiantes", "7.Salir" };

        ArrayList<String[]> estudiantes = new ArrayList<>();
        Scanner sc = new Scanner(System.in);
        String eleccion;
        boolean salir = false;
        while (salir != true) {
            for (String opcion : menu) {
                System.out.println(opcion);
            }
            System.out.println("Elige la funcion a realizar");
            eleccion = sc.nextLine();

            switch (eleccion) {
                case "1":
                    System.out.println("Dame el nombre del alumno");
                    sc.nextLine();
                    String nombre = sc.nextLine();
                    System.out.println("Escribe la edad del alumno");
                    String edad = sc.nextLine();
                    edad=leerNumeroPositivo(sc, edad);
                    System.out.println("Escribe la nota final del alumno");
                    String notafinal = sc.nextLine();
                    notafinal=notaValida(sc, notafinal);
                    String[] estudiante = { nombre, edad, notafinal };
                    estudiantes.add(estudiante);
                    break;
                case "2":
                    listar(estudiantes);
                    break;
                case "3":
                    listar(estudiantes);
                    if (estudiantes.size() > 0) {
                        System.out.println("Escribe el nombre del alumno a cambiar. ");
                        sc.nextLine();
                        String alumnoCambio = sc.nextLine();
                        for (int i = 0; i < estudiantes.size(); i++) {
                            String[] a = estudiantes.get(i);
                            if (a[0].equals(alumnoCambio)) {
                                System.out.println("¿Cuantos años tiene?");
                                String edadNueva = sc.nextLine();
                                edadNueva = leerNumeroPositivo(sc, edadNueva);
                                System.out.println("Escribe su nueva nota");
                                String notaNueva = sc.nextLine();
                                notaNueva = notaValida(sc, notaNueva);
                                String[] cambio = { alumnoCambio, edadNueva, notaNueva };
                                estudiantes.set(i, cambio);
                                break;
                            }
                        }
                    }
                    break;
                case "4":
                    listar(estudiantes);
                    System.out.println("Escribe el nombre del alumno a eliminar. ");
                    sc.nextLine();
                    String alumnoBorrar = sc.nextLine();
                    boolean flag = false;
                    for (int i = 0; i < estudiantes.size(); i++) {
                        String[] a = estudiantes.get(i);
                        if (a[0].equals(alumnoBorrar)) {
                            estudiantes.remove(i);
                            System.out.println(String.format("Se ha eliminado a %s", a[0]));
                            flag = true;
                            break;
                        }
                    }
                    if (flag==false) {
                        System.out.println("No se encontro el alumno.");
                    }
                    break;
                case "5":
                    estudiantes.clear();
                    System.out.println("Se elimino correctamente todo el listado.\n");

                    break;
                case "6":
                    System.out.println("Alumnos aprobados=\n");
                    for(int i=0; i<estudiantes.size();i++){
                        String[] a=estudiantes.get(i);
                        Float nota= Float.parseFloat(a[2]);
                        if (nota>=5){
                             System.out.println(String.format("%d . %s: %s años. Nota:%s", i + 1, a[0], a[1], a[2]));
                        }
                    }
                    break;
                case "7":
                    System.out.println("¿Esta seguro de querer salir?[S/N]");
                    sc.nextLine();
                    String confirm=sc.nextLine();
                    if (confirm.equals("S")) {
                        salir=true;
                        System.out.println("Sayonara baby!");
                    }else if(confirm.equals("N")){
                        System.out.println("Devolviendo al menu");
                    }else{
                        System.out.println("No entendi la confirmacion. Devolviendo al menu");
                    }
                    
                    break;

                default:
                    System.out.println("Comando no reconocido. Intenta de nuevo");
                    break;
            }// Final switch case

        } // Final while
    }// final main








//==============================Funciones ======================================================================= 
    public static String leerNumeroPositivo(Scanner sc, String mensaje) {
        float numero;
        boolean esValido = false;

        while (!esValido) {
            try {
                numero = Float.parseFloat(mensaje); // Intentamos la conversión

                if (numero >= 0 ) {
                    esValido = true;
                }  else  {
                    System.out.println("Error: El número debe ser positivo (mayor o igual a 0 y menor a 10).");
                    System.out.print("Inténtalo de nuevo: ");
                    mensaje = sc.nextLine();
                }

            } catch (NumberFormatException e) {
                // Si Float.parseFloat falla, cae aquí:
                System.out.println("Error: '" + mensaje + "' no es un número válido. Inténtalo de nuevo.");
                System.out.print("Inténtalo de nuevo: ");
                    mensaje = sc.nextLine();
            }
        }
        return mensaje;
    }
    public static String notaValida(Scanner sc, String mensaje) {
        float numero;
        boolean esValido = false;

        while (!esValido) {
            try {
                numero = Float.parseFloat(mensaje); // Intentamos la conversión

                if (numero >= 0 &&  numero<=10) {
                    esValido = true;
                }  else  {
                    System.out.println("Error: El número debe ser positivo (mayor o igual a 0 y menor a 10).");
                    System.out.print("Inténtalo de nuevo: ");
                    mensaje = sc.nextLine();
                }
                

            } catch (NumberFormatException e) {
                // Si Float.parseFloat falla, cae aquí:
                System.out.println("Error: '" + mensaje + "' no es un número válido. Inténtalo de nuevo.");
                System.out.print("Inténtalo de nuevo: ");
                    mensaje = sc.nextLine();
            }
        }
        return mensaje;
    }

    public static void listar(ArrayList<String[]> estudiantes) {
        if (estudiantes.size() > 0) {
            for (int i = 0; i < estudiantes.size(); i++) {
                String[] alumno = estudiantes.get(i);
                System.out.println(String.format("%d . %s: %s años. Nota:%s", i + 1, alumno[0], alumno[1], alumno[2]));

            }
        } else {
            System.out.println("Lista vacia. Añade un Alumno y sus datos");
        }
    }

}
