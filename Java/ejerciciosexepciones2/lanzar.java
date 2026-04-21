package ejerciciosexepciones2;

public class lanzar {
    public static void main(String[] args) {
        int num=-5;

        if (num < 0) {
            throw new IllegalArgumentException("El número no puede ser negativo");
        }
        System.out.println("Número válido: " + num);
    }
}
