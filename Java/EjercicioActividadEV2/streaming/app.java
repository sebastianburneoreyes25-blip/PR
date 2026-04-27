package EjercicioActividadEV2.streaming;

import java.util.Scanner;

public class app {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Introduce el título: ");
        String titulo = sc.nextLine();
        System.out.print("Introduce la calidad (720, 1080, 4000): ");
        int calidad = sc.nextInt();
        if (calidad != 720 && calidad != 1080 && calidad != 4000) {
            System.out.println("Calidad no válida. Se asigna 720 por defecto.");
            calidad = 720;
        }
        Reproducible contenido = new Pelicula(titulo, 120, calidad);
        int opcion;
        do {
            System.out.println("\nMenú:");
            System.out.println("1. Play");
            System.out.println("2. Pause");
            System.out.println("3. Stop");
            System.out.print("Elige una opción: ");
            opcion = sc.nextInt();

            switch (opcion) {
                case 1:
                    contenido.play();
                    break;
                case 2:
                    contenido.pause();
                    break;
                case 3:
                    contenido.stop();
                    System.out.println("Saliendo...");
                    break;
                default:
                    System.out.println("Opción no válida.");
            }

        } while (opcion != 3);

        sc.close();
    }
}
