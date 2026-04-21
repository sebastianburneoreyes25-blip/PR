package ejerciciosexepciones2;

public class temp {
    public static void main(String[] args) {
        
        class TemperaturaInvalidaException extends Exception {
        public TemperaturaInvalidaException(String mensaje) {
            super(mensaje);
        }
    }

        int temperatura = 60; // prueba

        try {
            if (temperatura < -50 || temperatura > 50) {
                throw new TemperaturaInvalidaException("Temperatura fuera de rango: " + temperatura);
            }
            System.out.println("Temperatura válida: " + temperatura);
        } catch (TemperaturaInvalidaException e) {
            System.out.println(e.getMessage());
        }
    }
}
