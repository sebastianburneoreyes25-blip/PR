package Java.EjerciciosPOOestudio.GestionDePaquetes;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class app {
    public static void main(String[] args) {

        ArrayList<String> menu=new ArrayList<>();
        Collections.addAll(menu, "1.Registrar paquete","2.Registrar datos de los repartidores",
        "3.Asignar paquete a repartidores", "4.Mostrar estado de paquetes","5.Mostrar incidencias",
        "6.Mostrar infromes de rendimiento", "7.Reasignar paquete","8.Salir");
        ArrayList<Paquetes> listaPaquetes=new ArrayList<>();
        ArrayList<Repartidor> repartidores=new ArrayList<>();+
        String eleccion ="";
        showMenu(menu);
        Scanner sc=new Scanner(System.in);
        eleccion=sc.nextLine();
        switch (eleccion) {
            case "1":
                System.out.println("Escribe el id, recuerda que debe ser unico y numero entero");
                int id=sc.nextInt();
                System.out.println("Escribe el destino");
                String destino=sc.nextLine();
                System.out.println("Escribe el peso del paquete");
                Paquetes
                
                break;
        
            default:
                break;
        }




}
    
    public static void showMenu(ArrayList menu){
        for(int i=0;i<menu.size();i++){
        System.out.println(menu.get(i));
        System.out.println("Elige una opcion");

        }
    }

}
