package EjercicioActividadEV2.climatizacionInteligente;


public class Humidificador extends DispositivoClimatico{
    
     public Humidificador(Sensor[] sensores) {
        super(sensores);
    }

    @Override
    public void analizarEntorno() {
        double promedio = calcularPromedio();
        if (promedio < 30) {
            System.out.println("Añadiendo humedad");
        } else {
            System.out.println("No es necesario añadir humedad");
        }
    }
}
