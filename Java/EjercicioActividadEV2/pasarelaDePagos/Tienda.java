package EjercicioActividadEV2.pasarelaDePagos;

public class Tienda {
    
    public void ejecutarCobro(MetodoPago metodo, double total) {
        metodo.procesarPago(total);
    }
}
