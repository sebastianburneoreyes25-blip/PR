package Java.EjerciciosClases;

public class Product {
    String producto;
    float precio;

    public Product(String producto, float precio){
        this.producto=producto;
        this.precio=precio;
    }

    public void descuento(){
        System.out.println("Se va a aplicar un 5% de descuento al producto");
        float precioOld=this.precio;
        this.precio=this.precio*0.95f;
        System.out.println(String.format("El producto antes valia %.2f y ahora %.2f ", precioOld, this.precio));
        
    }
}
