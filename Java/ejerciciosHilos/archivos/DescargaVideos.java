package ejerciciosHilos.archivos;

public class DescargaVideos extends Thread{
    @Override
    public void run(){
        for(int i=0;i<=100;i+=10){
            System.out.println("Descargando video ....."+i+"%");
            try{
                Thread.sleep(1300);
            }catch(InterruptedException e){
                System.out.println("Descarga cancelada");
            }

        }
    }
}
