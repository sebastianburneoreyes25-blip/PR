package ejerciciosHilos.contadorReloj;

public class Contador extends Thread {
    

    @Override
    public void run(){
        for(int i=1;i<=10;i++){
            System.out.println("Contados: "+i);

            try{
                Thread.sleep(500);
            }catch(InterruptedException e){
                System.out.println("Error: "+e.getMessage() );
            }

        }
    }


}
