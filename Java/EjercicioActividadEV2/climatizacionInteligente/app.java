package EjercicioActividadEV2.climatizacionInteligente;

import java.util.Scanner;

public class app {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Sensor[] sensores = new Sensor[3];

        System.out.println("Introduce los valores de los sensores:");

        for (int i = 0; i < 3; i++) {
            System.out.print("Sensor " + (i + 1) + ": ");
            double valor = scanner.nextDouble();
            sensores[i] = new Sensor(valor);
        }
        AireAcondicionado aire = new AireAcondicionado(sensores);
        Humidificador humidificador = new Humidificador(sensores);
        System.out.println("\n--- Resultado ---");
        aire.analizarEntorno();
        humidificador.analizarEntorno();

        scanner.close();
    }
}
