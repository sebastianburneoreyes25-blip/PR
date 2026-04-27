package EjercicioActividadEV2.gestionTransporte;

import java.util.Scanner;

public class app {
    
    public static void main(String[] args) {
        System.out.println("Vamos a empezar por el motor del camion. Escribe el tipo de combustible que usa");
        Scanner sc=new Scanner(System.in);
        String combustibleCam =sc.nextLine();
        System.out.println("Ahora los caballos del motor ");
        sc.nextLine();
        int caballosCam=sc.nextInt();
        Motor motorCamion=new Motor(caballosCam, combustibleCam);
        System.out.println("Escribe el id del camion(numerico)");
        int id =sc.nextInt();
        System.out.println("Escribe la capacidad de carga");
        double capacidad=sc.nextDouble();
        Camion camion=new Camion(id, capacidad, motorCamion);
        System.out.println("Escribe cuantos km hace");
        double km=sc.nextDouble();
        camion.calcularCosteRuta(km);
        System.out.println("Vamos a seguir por el motor de la furgoneta. Escribe el tipo de combustible que usa");
      
        String combustibleFurg =sc.nextLine();
        System.out.println("Ahora los caballos del motor ");
        sc.nextLine();
        int caballosFurg=sc.nextInt();
        Motor motorFurg=new Motor(caballosFurg, combustibleFurg);
        System.out.println("Escribe el id de la furgoneta(numerico)");
        int idFurg =sc.nextInt();
        System.out.println("Escribe la capacidad de carga");
        double capacidadFurg=sc.nextDouble();
        Furgoneta furgoneta=new Furgoneta(idFurg, capacidadFurg, motorFurg);
        System.out.println("Escribe cuantos km hace");
        double kmFurg=sc.nextDouble();
        furgoneta.calcularCosteRuta(kmFurg);
        sc.close();




    }
}
