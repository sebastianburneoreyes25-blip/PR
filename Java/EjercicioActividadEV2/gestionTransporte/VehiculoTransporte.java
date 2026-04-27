package EjercicioActividadEV2.gestionTransporte;



public abstract class VehiculoTransporte {
    
    int id;
    double capacidadCarga;
    Motor motor;

    public VehiculoTransporte(int id, double capacidad, Motor motor){
        if (motor == null) {
            throw new IllegalArgumentException("El motor es obligatorio");
        }
        this.id = id;
        this.capacidadCarga = capacidad;
        this.motor = motor;
    }

    public  abstract double calcularCosteRuta(double km);

}
