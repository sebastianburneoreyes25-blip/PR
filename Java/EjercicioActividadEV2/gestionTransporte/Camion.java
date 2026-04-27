package EjercicioActividadEV2.gestionTransporte;

public class Camion extends VehiculoTransporte {

    public Camion(int id, double capacidadCarga, Motor motor) {
        super(id, capacidadCarga, motor);
    }

    @Override
    public double calcularCosteRuta(double km) {
        return km * 2.5 + capacidadCarga;
    }
}
