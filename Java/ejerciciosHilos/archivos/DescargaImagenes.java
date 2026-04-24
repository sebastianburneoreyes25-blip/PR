package ejerciciosHilos.archivos;

public class DescargaImagenes extends Thread{
    
    @Override 
    public void run(){
        for(int i=0; i<=100;i+=10){
            System.out.println("Descargando imagen ......"+i+"%");

            try{
                Thread.sleep(700);
            }catch(InterruptedException e){
                System.out.println("Descarga interrumpida");
            }
        }
    }

}
