package EjercicioActividadEV2.gestionTransporte;

public class Furgoneta extends VehiculoTransporte {
    
    public Furgoneta(int id, double capacidadCarga, Motor motor) {
        super(id, capacidadCarga, motor);
    }

    @Override
    public double calcularCosteRuta(double km) {
        return km * 1.5;
}
}
