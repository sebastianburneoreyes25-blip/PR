package hilos;

public class Proceso1 extends Thread {
    public void run(){
        for(int i=0;i<=5;i++){
            System.out.println("Proceso 1");
        }
    }
    
}
