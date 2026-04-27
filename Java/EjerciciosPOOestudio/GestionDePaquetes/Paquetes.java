package Java.EjerciciosPOOestudio.GestionDePaquetes;

import java.util.ArrayList;
import java.util.Scanner;

public class Paquetes {
    int id;
    String destino;
    float peso;
    boolean prioridad;
    String estado="En preparacion";
    Repartidor repartidorAsignado=null;

    public Paquetes(
    int id, String destino, float peso, boolean prioridad, 
    ArrayList<Paquetes> paquetes,Scanner sc){
            if(paquetes.size()>0){
                id=this.idValido(sc, paquetes, id);
            }
            this.id=id;
            this.destino=destino;
            this.prioridad=prioridad;
            this.peso=peso;
           
    }

    public static ArrayList<Paquetes> registrarPaquete(ArrayList<Paquetes> listaPaquetes, Scanner sc){
        System.out.println("Escribe el id, recuerda que debe ser unico y numero entero");
        int id=sc.nextInt();
        System.out.println("Escribe el destino");
        String destino=sc.nextLine();
        System.out.println("Escribe el peso del paquete");
        float peso=sc.nextFloat();
        peso=Paquetes.pesoValido(peso, sc);
        System.out.println("¿Es prioritario? presiona 1 para si 0 para no.");
        boolean prioridad;
        prioridad= Paquetes.priodidadEleccion(sc);
        System.out.println("Se va a añadir el paquete: "+id+" "+destino+" "+peso+" "
        +prioridad+"\n"+ "Pulsa 1 para confirmar, 0 para cancelar");
        int confirmacion=sc.nextInt();
        if(confirmacion==1){
            Paquetes paquete=new Paquetes(id, destino, peso, prioridad, listaPaquetes, sc);
            listaPaquetes.add(paquete);
            System.out.println("Paquete agregado");
        }else{
            System.out.println("Cancelado el registro.");
        }
    return listaPaquetes;
    }

    private int idValido(Scanner sc, ArrayList<Paquetes> listaPaquetes, int id){
        
        boolean salirBucle=false;
        while (salirBucle!=true) {
            boolean valido=true;
            for(Paquetes pack:listaPaquetes){
            if(pack.id==id){
                valido=false;
            }
        }
        if(valido==false){
            System.out.println("El id no es valido, ya existe. Intentelo de nuevo");
            sc.nextLine();
            id=sc.nextInt();
        }  else{
            salirBucle=true;
        }
        }
        return id;
    }

    public static float pesoValido(float peso, Scanner sc){
        while (peso<0) {
            System.out.println("Se necesita que el peso sea un numero positivo");
            peso=sc.nextFloat();
        }
        return peso;
    }

    
    public static boolean priodidadEleccion(Scanner sc){
        var eleccion=sc.nextInt();
        boolean prioridad;
        if(eleccion==0){
            prioridad=false;
            
        }else if (eleccion==1){
            prioridad=true;
            System.out.println("paquete asignado como prioritario");
        }else{
            System.out.println("comando no reconocido. Paquete no prioritario pòr defecto.");
            prioridad=false;
        }

        return prioridad;
    }

    public void asignarRepartidor(Repartidor r){
        repartidorAsignado=r;
    }
}

