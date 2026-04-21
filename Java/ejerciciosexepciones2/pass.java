package ejerciciosexepciones2;

public class pass {
    public static void main(String[] args) {
        
        String pass="holi";
        if (pass == null || pass.length() < 6) {
            throw new IllegalArgumentException("La contraseña es demasiado corta");
        }
        System.out.println("Contraseña válida");
    }
}
