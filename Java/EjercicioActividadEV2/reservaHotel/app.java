package EjercicioActividadEV2.reservaHotel;

import java.util.Scanner;

public class app {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 1. Pedir datos del cliente
        System.out.print("Introduce nombre del cliente: ");
        String nombre = scanner.nextLine();

        System.out.print("Introduce DNI del cliente: ");
        String dni = scanner.nextLine();

        Cliente cliente = new Cliente(nombre, dni);

        // 2. Preguntar tipo de habitación
        System.out.print("Introduce número de habitación: ");
        int numero = scanner.nextInt();

        System.out.print("Introduce precio base: ");
        double precioBase = scanner.nextDouble();

        System.out.println("Tipo de habitación (1: Simple, 2: Suite): ");
        int tipo = scanner.nextInt();

        Habitacion habitacion;

        // 3. Validación para Suite
        if (tipo == 2) {
            System.out.print("Introduce coste del minibar: ");
            double minibar = scanner.nextDouble();
            habitacion = new HabitacionSuite(numero, precioBase, minibar);
        } else {
            habitacion = new HabitacionSimple(numero, precioBase);
        }

        Reserva reserva = new Reserva(cliente, habitacion);

        // 4. Imprimir factura
        reserva.imprimirFactura();

        scanner.close();
    }
}
