package ejerciciosInterfaces.ejercicio3;

class Rectangulo extends Forma {
    private double base, altura;

    public Rectangulo(double base, double altura) {
        this.base = base;
        this.altura = altura;
    }

    public double calcularArea() {
        return base * altura;
    }
}