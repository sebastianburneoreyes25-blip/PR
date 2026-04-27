package EjercicioActividadEV2.sensoresIndustriales;

public class SensorPres extends Sensor implements Alerta{
    
   public SensorPres(int id, double valorActual){
        super(id, valorActual);
    }

    @Override
    public void evaluarRiesgo(double valorActual){
         if (valorActual > 50) {
            System.out.println(id + " -> PELIGRO: Explosion");
        }

    }

}
