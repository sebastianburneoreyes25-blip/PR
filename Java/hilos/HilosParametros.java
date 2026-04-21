package hilos;

public class HilosParametros extends Thread {
    int num;


    @Override
    public void run() {
        for (int i = 0; i <= this.num; i++) {
            System.out.println(i);
        }
        System.out.println("");
    }

    public void valorCondicion(int valor){
        this.num=valor;

    }
}
