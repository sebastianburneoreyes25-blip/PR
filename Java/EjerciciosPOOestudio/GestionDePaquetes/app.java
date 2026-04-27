package Java.EjerciciosPOOestudio.GestionDePaquetes;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class app {
    public static void main(String[] args) {

        ArrayList<String> menu=new ArrayList<>();
        Collections.addAll(menu, "1.Registrar paquete","2.Registrar datos de los repartidores",
        "3.Asignar/Reasignar paquete a repartidores", "4.Mostrar estado de paquetes","5.Mostrar incidencias",
        "6.Mostrar infromes de rendimiento", "8.Salir");
        ArrayList<Paquetes> listaPaquetes=new ArrayList<>();
        ArrayList<Repartidor> repartidores=new ArrayList<>();
        String eleccion ="";
        showMenu(menu);
        Scanner sc=new Scanner(System.in);
        eleccion=sc.nextLine();
        while (eleccion!="8") {
            switch (eleccion) {
            case "1":
                listaPaquetes=Paquetes.registrarPaquete(listaPaquetes, sc);
                break;
            case "2":
                repartidores=Repartidor.registrarRepartidor(repartidores, sc);
                break;
            
            case "3":
            System.out.println("Escribe el id del repartidor");
            int idRep=sc.nextInt();
            boolean foundDel=false;
            boolean foundPak=false;
            for (Repartidor repartidor : repartidores) { 
                if(repartidor.id==idRep){
                    foundDel=true;
                    System.out.println("Escribe el id del paquete");
                    int paqueteId=sc.nextInt();
                    for (Paquetes paquete : listaPaquetes) {
                        if(paquete.id==paqueteId && paquete.repartidorAsignado==null){
                            foundPak=true;
                            paquete.asignarRepartidor(repartidor);
                            paquete.estado="Asignado";
                            repartidor.agregarPaquete(paquete);
                        }else if(paquete.id==paqueteId && paquete.repartidorAsignado!=null){
                            Repartidor repartidorOld=paquete.repartidorAsignado;
                            Repartidor.cambiarRepartidor(listaPaquetes,repartidorOld,paquete);
                            foundPak=true;
                            paquete.asignarRepartidor(repartidor);
                            paquete.estado="Reasignado";
                            repartidor.agregarPaquete(paquete);
                        }
                            }
                        }
                    }
                    if(foundDel==true && foundPak==true ){
                        System.out.println("Paquete asignado correctamente.");
                    }else  {
                        System.out.println("Paquete/Repartidor no encontrado. Pruebe de nuevo");
                    }

                break;
            
            default:
                break;
        }//fin switch
        showMenu(menu);
        eleccion=sc.nextLine();
        }//fin while
}//fin main
    
    public static void showMenu(ArrayList<String> menu){
        for(int i=0;i<menu.size();i++){
        System.out.println(menu.get(i));
        System.out.println("Elige una opcion");

        }
    }

}
