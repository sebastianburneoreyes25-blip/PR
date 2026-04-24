package ejerciciosHilos.cajero;

public class CuentaBancaria {
      private int saldo;

    public CuentaBancaria(int saldoInicial) {
        this.saldo = saldoInicial;
    }

    // Método sincronizado → evita accesos simultáneos
    public synchronized void retirar(String nombre, int cantidad) {

        if (saldo >= cantidad) {
            System.out.println(nombre + " va a retirar " + cantidad);

            try {
                Thread.sleep(500); // simula tiempo de operación
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            saldo -= cantidad;
            System.out.println(nombre + " retiró " + cantidad + " | Saldo restante: " + saldo);

        } else {
            System.out.println(nombre + " intentó retirar " + cantidad + " pero NO hay saldo suficiente. Saldo: " + saldo);
        }
    }
}
