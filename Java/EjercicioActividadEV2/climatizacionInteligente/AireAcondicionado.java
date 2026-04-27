package EjercicioActividadEV2.climatizacionInteligente;

public class AireAcondicionado extends DispositivoClimatico {
    
    public AireAcondicionado(Sensor[] sensores) {
        super(sensores);
    }

    @Override
    public void analizarEntorno() {
        double promedio = calcularPromedio();
        if (promedio > 25) {
            System.out.println("Enfriando");
        } else {
            System.out.println("No es necesario enfriar");
        }
    }

}
