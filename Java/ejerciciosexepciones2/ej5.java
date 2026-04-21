package ejerciciosexepciones2;

public class ej5 {
    
    public static void main(String[] args) {
        try {
            int resultado = 10 / 0;
        } catch (ArithmeticException e) {
            System.out.println("Error: división por cero");
        } finally {
            System.out.println("Este bloque siempre se ejecuta");
        }
    }
}
