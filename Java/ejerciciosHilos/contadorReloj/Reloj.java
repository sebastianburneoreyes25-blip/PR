package ejerciciosHilos.contadorReloj;

import java.time.LocalTime;
import java.time.format.DateTimeFormatter;

public class Reloj extends Thread{
    
    @Override
    public void run(){
         DateTimeFormatter formato = DateTimeFormatter.ofPattern("HH:mm:ss");
        int i=0;
        while (i<15) {
            LocalTime ahora = LocalTime.now();
            System.out.println("Hora actual: " + ahora.format(formato));
            i++;
            try {
                Thread.sleep(1000); // pausa de 1 segundo
            } catch (InterruptedException e) {
                System.out.println("Hilo reloj interrumpido");
                break;
            }
    }

}
}
