package ejerciciosHilos.ArrayDiv;

public class BuscadorMax extends Thread {
    private int[] arreglo;
    private int inicio; 
    private int fin;
    private int maximo;

    public BuscadorMax(int[] arreglo, int inicio, int fin) {
        this.arreglo = arreglo;
        this.inicio = inicio;
        this.fin = fin;
        this.maximo = Integer.MIN_VALUE;
    }

    @Override
    public void run() {
        for (int i = inicio; i < fin; i++) {
            if (arreglo[i] > maximo) {
                maximo = arreglo[i];
            }
        }
        System.out.println("Máximo encontrado en rango [" + inicio + ", " + fin + "): " + maximo);
    }

    public int getMaximo() {
        return maximo;
    }
}
