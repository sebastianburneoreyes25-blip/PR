package Java.EjerciciosClases;

public class Rectangle {
    float base;
    float altura;
    float area;
    float perimetro;


    public Rectangle(float base,float altura){
        this.base=base;
        this.altura=altura;
        

    }

    public void calcularArea(){
        this.area=(base*altura);
        System.out.println("Area="+this.area);
    }

    public void calcularPerimetro(){
       this.perimetro=this.area*2;
       System.out.println( "Perimetro ="+this.perimetro);
    }
}
