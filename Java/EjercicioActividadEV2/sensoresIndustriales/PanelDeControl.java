package EjercicioActividadEV2.sensoresIndustriales;


public class PanelDeControl {
    
    Sensor[] sensores=new Sensor[4];

    public void setSensores(int i, Sensor s){
        this.sensores[i]=s;
    }

}
