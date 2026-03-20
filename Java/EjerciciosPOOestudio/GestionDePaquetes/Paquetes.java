package Java.EjerciciosPOOestudio.GestionDePaquetes;

import java.util.ArrayList;
import java.util.Scanner;

public class Paquetes {
    int id;
    String destino;
    float peso;
    boolean prioridad;
    String estado;

    public Paquetes(
    int id, String destino, float peso, boolean prioridad,String estado, 
    ArrayList<Paquetes> paquetes,Scanner sc){
            if(paquetes.size()>0){
                id=this.idValido(sc, paquetes, id);
            }
            this.id=id;
            this.destino=destino;
            this.prioridad=prioridad;
            this.peso=peso;
            this.estado=estado;

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


}
