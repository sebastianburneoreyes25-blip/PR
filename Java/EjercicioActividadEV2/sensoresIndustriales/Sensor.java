package EjercicioActividadEV2.sensoresIndustriales;

import java.util.Scanner;

public abstract class Sensor {
    
    int id;
    double valorActual;

    public Sensor(int id, double valorActual){
        while(id<0){
            System.out.println("No puede ser un id. Introduce de nuevo");
            Scanner sc=new Scanner(System.in);
            id=sc.nextInt();
            sc.close();
        }
        this.id=id;
        while(valorActual<0){
            System.out.println("No puede ser un valor negativo. Introduce de nuevo");
            Scanner sc=new Scanner(System.in);
            valorActual=sc.nextDouble();
            sc.close();
        }
        this.valorActual=valorActual;

    }

}
