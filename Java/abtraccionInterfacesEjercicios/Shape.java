package abtraccionInterfacesEjercicios;



public abstract class Shape {

    void calcularArea(){
        System.out.println("Area de la figura");
    }

    public static class  Circle extends Shape {
    
        int radio=5;

        @Override
        void calcularArea(){
            System.out.println("Aqui la formula del area del circulo: pi*radio^2");
            System.out.println("Area:"+this.radio*3.14);
        }
        
    }
    public static class Rectangle extends Shape {
    
        int lado1=10;//Estos valores se asignarian de normal en el codigo, no se definirian en la clase
        int lado2=5;

        @Override
        void calcularArea(){
            System.out.println("Aqui la formula del area del Rectangulo: lado1*lado2");
            System.out.println("Area:"+this.lado1*lado2);
        }
        
    }

    public static void main(String[] args) {
        Circle circle=new Circle();
        Rectangle rectangle = new Rectangle();
        circle.calcularArea();
        rectangle.calcularArea();
    }
    
}
