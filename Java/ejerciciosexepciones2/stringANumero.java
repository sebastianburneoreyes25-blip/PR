package ejerciciosexepciones2;

public class stringANumero {

    public static void main(String[] args) {
        String texto;
        texto="15a";
        int num;
        try {
           num=Integer.parseInt(texto);
        } catch (NumberFormatException e) {
            System.out.println("Entrada no válida: " + texto+ "Error: "+e.getMessage());
        }
    }
    
}
