package EjercicioActividadEV2.sensoresIndustriales;

public class SensorTemp extends Sensor implements Alerta{
    
    
    public SensorTemp(int id, double valorActual){
        super(id, valorActual);
    }

    @Override
    public void evaluarRiesgo(double valorActual){
         if (valorActual > 100) {
            System.out.println(id + " -> PELIGRO: Incendio");
        }

    }

    

}
