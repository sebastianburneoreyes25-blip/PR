package ejerciciosHilos.ArrayDiv;

import java.util.Random;

public class GeneradorArreglo {
    public static int[] generar(int tamaño) {
        int[] arreglo = new int[tamaño];
        Random random = new Random();

        for (int i = 0; i < tamaño; i++) {
            arreglo[i] = random.nextInt(10000); // números entre 0 y 9999
        }

        return arreglo;
}
}