package EjercicioActividadEV2.sensoresIndustriales;

import java.util.Scanner;

public class app {
    
    public static void main(String[] args) {
        PanelDeControl panel=new PanelDeControl();
        for(int i=0;i<4;i++){
            if(i<2){
                System.out.println("Dame el id del sensor temperatua");
                Scanner sc=new Scanner(System.in);
                int id=sc.nextInt();
                System.out.println("Escribe la temperatura actual");
                double valor=sc.nextDouble();
                SensorTemp sensorTemp=new SensorTemp(id, valor);
                sensorTemp.evaluarRiesgo(valor);
                panel.setSensores(i, sensorTemp);
                sc.close();
            }else{
                System.out.println("Dame el id del sensor presion");
                Scanner sc=new Scanner(System.in);
                int id=sc.nextInt();
                System.out.println("Escribe la presion actual");
                double valor=sc.nextDouble();
                SensorPres SensorPres=new SensorPres(id, valor);
                SensorPres.evaluarRiesgo(valor);
                panel.setSensores(i, SensorPres);
                sc.close();
            }
        }
    }
}
