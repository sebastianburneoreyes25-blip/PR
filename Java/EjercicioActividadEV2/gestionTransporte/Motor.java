package EjercicioActividadEV2.gestionTransporte;

public class Motor {

    private int caballos;
    private String tipoCombustible;

    public Motor(int caballos, String tipoCombustible) {
        this.caballos = caballos;
        this.tipoCombustible = tipoCombustible;
    }

    public int getCaballos() {
        return caballos;
    }

    public String getTipoCombustible() {
        return tipoCombustible;
    }
    
}
