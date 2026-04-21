package ejerciciosexepciones2;

public class multicatch {
    
    public static void main(String[] args) {
        try {
            int[] numeros = {1, 2, 3};
            System.out.println(numeros[5]); // error de índice
            int resultado = 10 / 0; // error aritmético
        } catch (ArithmeticException e) {
            System.out.println("Error aritmético");
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Índice fuera de rango");
        }
    }
}
