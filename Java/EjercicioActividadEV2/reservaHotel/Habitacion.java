package EjercicioActividadEV2.reservaHotel;

public  abstract class Habitacion {
    int numero;
    double precioBase;

    public Habitacion(int numero, double precioBase) {
        this.numero = numero;
        this.precioBase = precioBase;
    }

    public int getNumero() {
        return numero;
    }

    public abstract double calcularPrecioFinal();
}
