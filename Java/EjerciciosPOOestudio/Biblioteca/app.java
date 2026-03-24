package Java.EjerciciosPOOestudio.Biblioteca;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class app {

    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        ArrayList<Libro> biblioteca=new ArrayList<>();
        ArrayList<String> menu=new ArrayList<>();
        Collections.addAll(menu,"1.Añadir libro", "2.Eliminar libro","3.Buscar por categoria",
        "4.Prestar/devolver libro","5.Salir");
        Biblioteca.mostrarMenu(menu);
        int eleccion= sc.nextInt();
        while (eleccion!=5) {
          switch (eleccion) {
            case 1:
                biblioteca=Biblioteca.añadirLibro(biblioteca, sc);
                break;
            case 2:
                biblioteca=Biblioteca.eliminarLibro(biblioteca, sc);
                break;
        
            case 3:
                Biblioteca.buscarCateg(biblioteca, sc);
                break;
        
            case 4:
                biblioteca= Biblioteca.prestarDevolver(biblioteca, sc);
                break;
        
            case 5:
                System.out.println("Sayonara baby!!");
                break;
        
            default:
                System.out.println("No entendi el comando.Prueba de nuevo");
                break;
        }
        Biblioteca.mostrarMenu(menu);
        eleccion= sc.nextInt();
            
        }
        





    }
    

    
}
