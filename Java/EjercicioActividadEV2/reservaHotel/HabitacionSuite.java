package EjercicioActividadEV2.reservaHotel;

public class HabitacionSuite extends Habitacion {
     private double servicioMiniBar;

    public HabitacionSuite(int numero, double precioBase, double servicioMiniBar) {
        super(numero, precioBase);
        this.servicioMiniBar = servicioMiniBar;
    }

    @Override
    public double calcularPrecioFinal() {
        return precioBase + servicioMiniBar;
    }
}
