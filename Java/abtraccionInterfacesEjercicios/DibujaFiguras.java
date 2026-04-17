package abtraccionInterfacesEjercicios;



public  class DibujaFiguras {
    
    public interface Drawable {
    void draw();
        
    }

    public static class Circle implements Drawable {
        @Override
        public void draw(){
            System.out.println("Asi se dibuja un circulo O ");
        }
    
        
    }
    public static class Rectangle implements Drawable {
        @Override
        public void draw(){
            System.out.println("Asi se dibuja un circulo [] ");

        }
    
        
    }
    public static class Triangle implements Drawable {
        @Override
        public void draw(){
            System.out.println("Asi se dibuja un circulo 🔺 ");
        }
    
        
    }
    public static void main(String[] args) {
        Circle c=new Circle();
        Triangle T=new Triangle();
        Rectangle r=new Rectangle();
        c.draw();
        T.draw();
        r.draw();

    }
    
}
