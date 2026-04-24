package ejerciciosHilos.contadorReloj;

public class app {

    public static void main(String[] args) {
        Contador contador = new Contador();
        Reloj reloj = new Reloj();
        contador.start();
        reloj.start();
    }

}
