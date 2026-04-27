package EjercicioActividadEV2.climatizacionInteligente;

public abstract class DispositivoClimatico {

    Sensor[] sensores = new Sensor[3];

    public DispositivoClimatico(Sensor[] sensores) {
        this.sensores = sensores;
    }

    // Método para calcular el promedio
    public double calcularPromedio() {
        double suma = 0;
        for (Sensor s : sensores) {
            suma += s.getValorActual();
        }
        return suma / sensores.length;
    }

    // Método abstracto
    public abstract void analizarEntorno();
}



