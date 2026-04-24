package ejerciciosHilos.ArrayDiv;

public class app {
    
      public static void main(String[] args) {

        int[] arreglo = GeneradorArreglo.generar(1000);

        int mitad = arreglo.length / 2;

        BuscadorMax hilo1 = new BuscadorMax(arreglo, 0, mitad);
        BuscadorMax hilo2 = new BuscadorMax(arreglo, mitad, arreglo.length);

        hilo1.start();
        hilo2.start();

        try {
            hilo1.join();
            hilo2.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        int maxGlobal = Math.max(hilo1.getMaximo(), hilo2.getMaximo());

        System.out.println("Máximo global del arreglo: " + maxGlobal);
    }
}
