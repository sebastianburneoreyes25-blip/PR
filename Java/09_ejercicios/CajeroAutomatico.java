
import java.util.Scanner;

public class CajeroAutomatico {

    public static void main(String[] args) {

        /*
         * Ejercicio de Cajero Automático (ATM)
         * El usuario debe introducir por teclado el saldo inicial de la cuenta.
         * El programa debe mostrar un menú de opciones que se repetirá hasta que el
         * usuario decida salir.
         * El saldo siempre debe mostrarse con dos decimales.
         * 
         * Opciones del menú
         * 
         * Consultar saldo
         * Muestra el saldo actual.
         * 
         * Depositar dinero
         * El usuario introduce una cantidad.
         * Esta cantidad se suma al saldo.
         * 
         * Retirar dinero
         * El usuario introduce una cantidad.
         * Solo se permite retirar si hay saldo suficiente.
         * 
         * Saldo promedio semanal
         * 
         * Calcula el saldo promedio de la semana
         * 
         * Salir
         * 
         * Antes de cerrar el programa debe aparecer:
         * ¿Está seguro que desea salir? (S/N)
         * Si responde S, el programa termina.
         * Si responde N, vuelve al menú.
         */
        System.out.println("Bienvenido a tu Cajero ATM");
        Scanner sc = new Scanner(System.in);
        System.out.println("Escribe el saldo actual\n");
        float saldo = sc.nextFloat();
        saldo = numeroPositivo(saldo, sc);

        String[] menu = { "1.Consultar saldo", "2.Depositar dinero", "3.Retirar dinero", "4.Saldo promedio semanal",
                "5.Salir" };

        boolean salir = false;

        while (salir != true) {
            for (String opcion : menu) {
                System.out.println(opcion + "\n");
            }
            int eleccion = sc.nextInt();
            switch (eleccion) {
                case 1:
                    mostrarSaldo(saldo);
                    break;
                case 2:
                    System.out.println("Escribe cuanto se va a depositar");
                    float deposito = sc.nextFloat();
                    deposito = numeroPositivo(deposito, sc);
                    saldo += deposito;
                    mostrarSaldo(saldo);
                    break;
                case 3:
                    System.out.println("¿Cuanto dinero se va a retirar?");
                    float retirar = sc.nextFloat();
                    retirar = numeroPositivo(retirar, sc);
                    while (saldo - retirar < 0) {
                        System.out.println(
                                "No se puede retirar más cantidad que el saldo actual.\nIntroduce de nuevo la cantidad retirar");
                        retirar = sc.nextFloat();
                        numeroPositivo(retirar, sc);
                    }
                    saldo -= retirar;
                    mostrarSaldo(saldo);
                    break;
                case 4:
                    float salarioPromedio = saldo / 7;
                    System.out.println(String.format("El salario promedio semanal es %.2f €", salarioPromedio));
                    break;
                case 5:
                    System.out.println("¿Seguro que quieres salir?\n (S/N)");
                    sc.nextLine();
                    String confirmacion = sc.nextLine();
                    while (confirmacion.length() > 1) {
                        System.out.println("La confirmacion debe ser S (si) /N(no)\n");
                        confirmacion = sc.nextLine();
                    }
                    confirmacion = confirmacion.toUpperCase();
                    switch (confirmacion) {
                        case "S":
                            System.out.println("Hasta luego :D");
                            salir = true;
                            break;
                        case "N":
                            System.out.println("Volviendo al menú principal.\n");
                            break;

                        default:
                            System.out.println("Opcion no reconocida. Volviendo al menú principal\n");
                            break;
                    }

                    break;

                default:
                    System.out.println("Comando no reconocido. \n");
                    break;
            }
        }
        sc.close();

    }

    public static void mostrarSaldo(float saldo) {
        System.out.println(String.format("Tu saldo actual es: %.2f €", saldo));
    }

    public static float numeroPositivo(float numero, Scanner sc) {
        while (numero < 0) {
            System.out.println("El numero introducido no puede ser negativo. Introduce el valor de nuevo\n");
            numero = sc.nextFloat();
        }
        return numero;
    }

}
