package EjercicioActividadEV2.streaming;

public class Pelicula  extends Contenido implements Reproducible{
    
    
    public Pelicula(String titulo, int duracion, int calidad) {
        super(titulo, duracion, calidad);
    }

    @Override
    public void play() {
        System.out.println("Reproduciendo película " + titulo + "...");
    }

    @Override
    public void pause() {
        System.out.println("Película en pausa.");
    }

    @Override
    public void stop() {
        System.out.println("Película detenida.");
    }
}
