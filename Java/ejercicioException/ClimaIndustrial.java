import java.util.Scanner;

public class ClimaIndustrial {
    
    public static void main(String[] args) {
        System.out.println("Temperatua del reactor:");
        Scanner sc=new Scanner(System.in);
        double temp=sc.nextDouble();
        try{
            SensorTermico.analizar(temp);
        }catch (Exception e){
            System.out.println("ERROR:"+e.getMessage());
        }
        sc.close();
    }




    public class SensorTermico {
        
        static void analizar(double temp) throws Exception{
            if(temp>50||temp<-50){
                throw new Exception("ALERTA CRITICA EN TEMPERATURA");
            }
        }
        
    }
}
