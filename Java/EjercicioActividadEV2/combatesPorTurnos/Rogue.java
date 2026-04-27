package EjercicioActividadEV2.combatesPorTurnos;

public class Rogue extends Personaje implements HabilidadEspecial {
    
    
    public Rogue(String nombre, int vida){
            super(nombre, vida);
        }

        @Override
        public void activarEspecial(Personaje objetivo) {
            int dano = 30 * 2;
            System.out.println(nombre + " usa ataque crítico!");
            objetivo.recibirDano(dano);
        }

}
