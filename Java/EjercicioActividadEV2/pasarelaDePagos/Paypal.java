package EjercicioActividadEV2.pasarelaDePagos;

import java.util.Scanner;

public class Paypal implements MetodoPago {
    
    private String email;

    @Override
    public void procesarPago(double importe) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Introduce tu correo electrónico: ");
        email = sc.nextLine();

        if (!email.contains("@")) {
            System.out.println("Error: correo inválido. Pago cancelado.");
            sc.close();
            return;
        }

        System.out.println("Pago de " + importe + "€ realizado con PayPal.");
        sc.close();

    }
}
