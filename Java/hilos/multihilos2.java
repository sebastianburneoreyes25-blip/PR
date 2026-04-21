package hilos;

public class multihilos2 {

    public static void main(String[] args) {
        HilosParametros hilo1 = new HilosParametros();
        HilosParametros hilo2 = new HilosParametros();

        hilo1.valorCondicion(8);
        hilo2.valorCondicion(2);

        hilo1.start();
        hilo2.start();
    }

}
