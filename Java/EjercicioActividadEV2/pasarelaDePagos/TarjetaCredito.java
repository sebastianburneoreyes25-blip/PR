package EjercicioActividadEV2.pasarelaDePagos;

import java.util.Scanner;

public class TarjetaCredito implements MetodoPago {

    private String numero;
    private String fechaCaducidad;

    @Override
    public void procesarPago(double importe) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Introduce el número de tarjeta (16 dígitos): ");
        numero = sc.nextLine();

        if (numero.length() != 16 || !numero.matches("\\d+")) {
            System.out.println("Error: número de tarjeta inválido. Pago cancelado.");
            sc.close();

            return;
        }

        System.out.print("Introduce la fecha de caducidad (MM/AA): ");
        fechaCaducidad = sc.nextLine();

        System.out.println("Pago de " + importe + "€ realizado con tarjeta.");
        sc.close();

    }
}
