package ejerciciosHilos.cajero;

public class app {
     public static void main(String[] args) {

        CuentaBancaria cuenta = new CuentaBancaria(100);

        Hijo hijoA = new Hijo("Hijo A", cuenta);
        Hijo hijoB = new Hijo("Hijo B", cuenta);

        hijoA.start();
        hijoB.start();
     }
    
}
