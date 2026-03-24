package Java.EjerciciosPOOestudio.Biblioteca;

public class Libro {
    String titulo;
    String autor;
    Integer anioPublicacion;
    String categoria;
    boolean disponible;

    public Libro(String titulo,String autor, Integer anioPublicacion, String categoria, boolean disponible){
        this.titulo=titulo;
        this.autor=autor;
        this.anioPublicacion=anioPublicacion;
        this.categoria=categoria;
        this.disponible=disponible;
    }

}
