package Java.EjerciciosPOOestudio.Biblioteca;

import java.util.ArrayList;
import java.util.Scanner;

public class Biblioteca {

    public static ArrayList<Libro> añadirLibro(ArrayList<Libro> biblioteca, Scanner sc) {
        System.out.println("Escribe el titulo del libro que quieres añadir.");
        sc.nextLine();
        String titulo = sc.nextLine();
        System.out.println("Escribe el autor");
        String autor = sc.nextLine();
        System.out.println("Escribe el año de publicacion");
        Integer anioPublicacion = sc.nextInt();
        System.out.println("Escribe la categoria del libro");
        sc.nextLine();
        String categoria = sc.nextLine();
        Libro libro = new Libro(titulo, autor, anioPublicacion, categoria, true);
        biblioteca.add(libro);
        System.out.println(libro.titulo+libro.autor+libro.anioPublicacion+libro.categoria);

        return biblioteca;
    }

    public static ArrayList<Libro> eliminarLibro(ArrayList<Libro> biblioteca, Scanner sc) {
        System.out.println("Escribe el nombre del libro a borrar");
        sc.nextLine();
        String eliminar = sc.nextLine();
        for (int i = 0; i < biblioteca.size(); i++) {
            Libro libro = biblioteca.get(i);
            if (libro.titulo.toUpperCase().equals(eliminar.toUpperCase())) {
                biblioteca.remove(i);
                System.out.println("Libro elimnado correctamente.");
            }
        }

        return biblioteca;
    }

    public static void buscarCateg(ArrayList<Libro> biblioteca, Scanner sc) {
        System.out.println("Escribe la categoria que quieres buscar");
        sc.nextLine();
        String buscar = sc.nextLine();
        for (int i = 0; i < biblioteca.size(); i++) {
            Libro libro = biblioteca.get(i);
            if (libro.categoria.toUpperCase().equals(buscar.toUpperCase())) {
                String disponible;
                if (libro.disponible == true) {
                     disponible = "Disponible"; 
                } else {
                     disponible = "No Disponible";
                }
                 System.out.println(
                            String.format("-%s %s, %s %s", libro.titulo, libro.autor, libro.categoria, disponible));
            }
        }

    }

    public static ArrayList<Libro> prestarDevolver(ArrayList<Libro> biblioteca, Scanner sc){

        System.out.println("Escribe el nombre del libro a borrar");
        sc.nextLine();
        String prestarDevolver = sc.nextLine();
        for(int i =0;i<biblioteca.size();i++){
            Libro libro=biblioteca.get(i);
            if(libro.titulo.toUpperCase().equals(prestarDevolver.toUpperCase())){
                boolean disponible;
                if(libro.disponible){
                    disponible=false;
                    System.out.println(String.format("Se ha prestado el libro %s ",libro.titulo));
                    libro.disponible=disponible;
                    biblioteca.set(i, libro);
                }else{
                    disponible=true;
                    System.out.println(String.format("Se ha devuelto el libro %s",libro.titulo));
                    libro.disponible=disponible;
                    biblioteca.set(i, libro);
                }

            }
        }


        return biblioteca;
    }


    public static void mostrarMenu(ArrayList<String> menu) {
        for (int i = 0; i < menu.size(); i++) {
            System.out.println(menu.get(i));
        }
        System.out.println("Elige una opcion");

    }

}
