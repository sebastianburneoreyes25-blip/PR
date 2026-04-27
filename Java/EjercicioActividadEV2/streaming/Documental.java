package EjercicioActividadEV2.streaming;

public class Documental extends Contenido implements Reproducible{
    
    public Documental(String titulo, int duracion, int calidad) {
        super(titulo, duracion, calidad);
    }

    @Override
    public void play() {
        System.out.println("Reproduciendo documental " + titulo + "...");
    }

    @Override
    public void pause() {
        System.out.println("Documental en pausa.");
    }

    @Override
    public void stop() {
        System.out.println("Documental detenido.");
    }

}
