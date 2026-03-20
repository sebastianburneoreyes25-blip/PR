package Java.EjerciciosClases;


public class Student {
    float score;

    public Student(float score){
        this.score=score;
    }

    public void aprobo(float score){
        if (score>=60){
            System.out.println("Ha aprobado");
        }else{
            System.out.println("No ha aprobado");
        }
    }
}
