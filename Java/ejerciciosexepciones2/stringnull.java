package ejerciciosexepciones2;

public class stringnull {

    public static void main(String[] args) {
        String texto = null;

        try {
            System.out.println("Longitud: " + texto.length());
        } catch (NullPointerException e) {
            System.out.println("Error: la variable String es nula");
        }
    }
    
}
