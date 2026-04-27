package EjercicioActividadEV2.combatesPorTurnos;

public class Paladin extends Personaje implements HabilidadEspecial {
    
    public Paladin(String nombre, int vida) {
        super(nombre, vida);
    }

    @Override
    public void activarEspecial(Personaje objetivo) {
        int curacion = 20;
        objetivo.vida += curacion;
        System.out.println(nombre + " cura a " + objetivo.nombre + " por " + curacion);
    }
}
