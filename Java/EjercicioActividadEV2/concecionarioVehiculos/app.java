package EjercicioActividadEV2.concecionarioVehiculos;

import java.util.Scanner;

public class app {
    public static void main(String[] args) {
        
        boolean finalizar=false;
        Coche coche=new Coche();
        System.out.println("Qur tipo de configuracion quieres? Normal (0) Extras (1)");
        Scanner sc=new Scanner(System.in);
        int opcion=sc.nextInt();
        while (finalizar==false) {
            switch (opcion) {
                case 0:
                    System.out.println("Escribe el color");
                    String color=sc.nextLine();
                    coche.configurar(color);
                    finalizar=true;
                    sc.close();
                    break;
            
                case 1:
                    boolean techo;
                    boolean nav;
                    System.out.println("Escribe el color");
                    color=sc.nextLine();
                    System.out.println("Tendra techo solar: Si(0)/No(1)");
                    int opcion2=sc.nextInt();
                    if (opcion2==0) {
                         techo=true;
                    }else   {
                         techo=false;
                    }
                    System.out.println("Tendra navegador: Si(0)/No(1)");
                     opcion2=sc.nextInt();
                    if (opcion2==0) {
                         nav=true;
                    }else   {
                         nav=false;
                    }
                    coche.configurar(color, techo, nav);
                    finalizar=true;
                    break;
                default:
                    System.out.println("No entendi el comando. Prueba de nuevo.\n¿Que tipo de configuracion quieres? Normal (1) Extras (0)");
                    opcion=sc.nextInt();
                    break;
            }
        }
        coche.mostrarDetalle();
    }
}
