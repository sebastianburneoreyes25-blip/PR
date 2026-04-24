package ejerciciosHilos.Mensajes;

import java.util.List;

public class Consumidor implements Runnable {

    private List<String> buffer;

    public Consumidor(List<String> buffer) {
        this.buffer = buffer;
    }

    @Override
    public void run() {
        
        int contador=0;
        while (contador<=15) {
            contador++;
            synchronized (buffer) {
                while (buffer.isEmpty()) {
                    try {
                        buffer.wait(); // espera si está vacío
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }

                String mensaje = buffer.remove(0);
                System.out.println("Consumido: " + mensaje);

                buffer.notifyAll(); // notifica al productor
            }

            try {
                Thread.sleep(800); 
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}