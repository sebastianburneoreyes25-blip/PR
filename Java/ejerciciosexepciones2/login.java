package ejerciciosexepciones2;

public class login {

    public class Main {
    // Excepción personalizada
    static class LoginFailedException extends Exception {
        public LoginFailedException(String mensaje) {
            super(mensaje);
        }
    }

    public static void main(String[] args) {
        String user = "admin";
        String pass = "1234";

        String inputUser = "admin";   // prueba
        String inputPass = "wrong";   // prueba

        try {
            if (!user.equals(inputUser) || !pass.equals(inputPass)) {
                throw new LoginFailedException("Usuario o contraseña incorrectos");
            }
            System.out.println("Login exitoso");
        } catch (LoginFailedException e) {
            System.out.println(e.getMessage());
        }
    }
}
    
}
