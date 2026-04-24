package ejerciciosHilos.Mensajes;

import java.util.List;

public class Productor implements Runnable {
 private List<String> buffer;
    private int maxSize;

    public Productor(List<String> buffer, int maxSize) {
        this.buffer = buffer;
        this.maxSize = maxSize;
    }

    @Override
    public void run() {
        int contador = 1;

        while (contador<=15) {
            synchronized (buffer) {
                while (buffer.size() == maxSize) {
                    try {
                        buffer.wait(); // espera si está lleno
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }

                String mensaje = "Mensaje " + contador++;
                buffer.add(mensaje);
                System.out.println("Producido: " + mensaje);

                buffer.notifyAll(); // notifica al consumidor
            }

            try {
                Thread.sleep(500); 
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
    }
    
}
    }
