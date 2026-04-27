package EjercicioActividadEV2.combatesPorTurnos;

public abstract class Personaje {
    int vida;
    String nombre;

    public Personaje(String nombre, int vida) {
        this.nombre = nombre;
        this.vida = vida;
    }

    public void recibirDano(int puntos) {
        vida -= puntos;
        System.out.println(nombre + " recibe " + puntos + " de daño.");
    }

    public void recibirDano(int puntos, String tipoArmadura) {
        if (tipoArmadura.equalsIgnoreCase("Escudo")) {
            puntos /= 2;
            System.out.println("Escudo activado! Daño reducido.");
        }
        recibirDano(puntos);
    }

    public boolean estaVivo() {
        return vida > 0;
    }
}
