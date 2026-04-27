package Java.EjerciciosPOOestudio.GestionDePaquetes;

import java.util.ArrayList;
import java.util.Scanner;

public class Repartidor {
    int id;
    String nombre;
    String zona;
    float capacidadMaxima;
    float capacidadActual=0;
    ArrayList<Paquetes> paquetesAsignados;

    public Repartidor(int id, String nombre,String zona,float capacidadMaxima, Scanner sc,
        ArrayList<Repartidor> repartidores){
            this.id=id;
            this.nombre=nombre;
            this.zona=zona;
            this.capacidadMaxima=capacidadMaxima;
            this.paquetesAsignados=new ArrayList<>();
            
    }

    public static ArrayList<Repartidor> registrarRepartidor(ArrayList<Repartidor> repartidores, Scanner sc){
        System.out.println("Escribe el id, recuerda que debe ser unico y numero entero");
        int idRepartidor=sc.nextInt();
        System.out.println("Escribe el nombre del repartidor");
        String nombre=sc.nextLine();
        System.out.println("Escribe la zona");
        String zona=sc.nextLine();
        System.out.println("Escribe la capacidad maxima del repartidor");
        float capacidad=sc.nextFloat();
        System.out.println("Se va a añadir el repartidor: "+idRepartidor+" "+nombre+" "
            +zona+" "+capacidad+"\n"+ "Pulsa 1 para confirmar, 0 para cancelar");
        int confirmacion=sc.nextInt();
        if(confirmacion==1){
            Repartidor repartidor=new Repartidor(idRepartidor, nombre, zona, capacidad, sc, repartidores);
            repartidores.add(repartidor);
            System.out.println("Repartidor agregado");
        }else{
            System.out.println("Cancelado el registro.");
        }
        return repartidores;
    }


    public void agregarPaquete(Paquetes p){
        if((this.capacidadActual+p.peso)>this.capacidadMaxima){
            System.out.println("No se puede agregar. Supera la capacidad maxima");
        }else { 
            this.capacidadActual=this.capacidadActual+p.peso;
            this.paquetesAsignados.add(p);
            
        }
    }

    public static void cambiarRepartidor(ArrayList<Paquetes> listaPa, Repartidor r,Paquetes p){
        for (Paquetes paquetes : listaPa) {
            if(paquetes.id==p.id){
                r.paquetesAsignados.remove(p);
                r.capacidadActual-=paquetes.peso;
            }
        }
    }
}
