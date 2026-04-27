package EjercicioActividadEV2.reservaHotel;

public class Reserva {
    private Cliente cliente;
    private Habitacion habitacion;

    public Reserva(Cliente cliente, Habitacion habitacion) {
        this.cliente = cliente;
        this.habitacion = habitacion;
    }

    public void imprimirFactura() {
        System.out.println("Cliente " + cliente.getNombre() +
                " con DNI " + cliente.getDni() +
                " ha reservado la habitación " + habitacion.getNumero() +
                " por un total de " + habitacion.calcularPrecioFinal() + "€");
    }
}
