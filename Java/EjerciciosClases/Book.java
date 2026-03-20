package Java.EjerciciosClases;
public class Book {

    String tittle;
    String author;

    public Book(String tittle, String author){
        this.tittle=tittle;
        this.author=author;
    }
    public void mostrar(){
        System.out.println(this.author+" "+this.tittle);
    }
    
}
