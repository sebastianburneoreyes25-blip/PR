package EjercicioActividadEV2.streaming;

public abstract class Contenido {
    String titulo;
    int duracion;
    int calidad;

    public Contenido(String titulo, int duracion, int calidad) {
        this.titulo = titulo;
        this.duracion = duracion;
        this.calidad = calidad;
    }
}
