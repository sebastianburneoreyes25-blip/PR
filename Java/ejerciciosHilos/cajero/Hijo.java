package ejerciciosHilos.cajero;

public class Hijo extends Thread{
      private CuentaBancaria cuenta;
    private String nombre;

    public Hijo(String nombre, CuentaBancaria cuenta) {
        this.nombre = nombre;
        this.cuenta = cuenta;
    }

    @Override
    public void run() {
        for (int i = 0; i < 5; i++) {
            cuenta.retirar(nombre, 20);
        }
    }
}
