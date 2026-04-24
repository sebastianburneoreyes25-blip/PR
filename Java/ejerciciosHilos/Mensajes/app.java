package ejerciciosHilos.Mensajes;

import java.util.ArrayList;
import java.util.List;

public class app {
     public static void main(String[] args) {

        List<String> buffer = new ArrayList<>();
        int maxSize = 5;

        Thread productor = new Thread(new Productor(buffer, maxSize));
        Thread consumidor = new Thread(new Consumidor(buffer));

        productor.start();
        consumidor.start();
    }
    
}
