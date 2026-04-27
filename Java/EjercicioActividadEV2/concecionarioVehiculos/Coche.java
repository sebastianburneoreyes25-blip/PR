package EjercicioActividadEV2.concecionarioVehiculos;

public class Coche {
    
    String color;
    Extras extras;

    public void configurar(String color){
        this.color=color;
    }

    public void configurar(String color,boolean techoSolar, boolean navegador ){
        this.color=color;
        this.extras=new Extras(techoSolar, navegador);
    }

    void mostrarDetalle(){
        System.out.println("El coche tiene: color "+this.color+" Extras: Techo solar"+extras.techoSolar+" Navegador: "+extras.navegador);
    }
}
