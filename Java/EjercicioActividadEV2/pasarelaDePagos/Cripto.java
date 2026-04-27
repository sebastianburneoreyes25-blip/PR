package EjercicioActividadEV2.pasarelaDePagos;

import java.util.Scanner;

public class Cripto implements MetodoPago {
     private String wallet;

    @Override
    public void procesarPago(double importe) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Introduce la dirección de la wallet: ");
        wallet = sc.nextLine();

        double comision = importe * 0.05;
        double total = importe + comision;

        System.out.println("Comisión del 5% aplicada: " + comision + "€");
        System.out.println("Pago total con cripto: " + total + "€");
        sc.close();

    }
}
