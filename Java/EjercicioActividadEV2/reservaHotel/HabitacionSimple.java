package EjercicioActividadEV2.reservaHotel;

public class HabitacionSimple extends Habitacion {
    
     public HabitacionSimple(int numero, double precioBase) {
        super(numero, precioBase);
    }

    @Override
    public double calcularPrecioFinal() {
        return precioBase;
    }
}
