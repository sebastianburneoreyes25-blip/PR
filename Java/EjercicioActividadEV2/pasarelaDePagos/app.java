package EjercicioActividadEV2.pasarelaDePagos;

import java.util.Scanner;

public class app {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Tienda tienda = new Tienda();

        System.out.print("Introduce el importe de la compra: ");
        double importe = sc.nextDouble();

        System.out.println("Selecciona método de pago:");
        System.out.println("1. Tarjeta de Crédito");
        System.out.println("2. PayPal");
        System.out.println("3. Cripto");

        int opcion = sc.nextInt();
        sc.nextLine(); // limpiar buffer

        MetodoPago metodo = null;

        switch (opcion) {
            case 1:
                metodo = new TarjetaCredito();
                break;
            case 2:
                metodo = new Paypal();
                break;
            case 3:
                metodo = new Cripto();
                break;
            default:
                System.out.println("Opción inválida.");
                sc.close();
                return;
        }

        // Polimorfismo en acción
        tienda.ejecutarCobro(metodo, importe);
        sc.close();

    }
    
    }

