import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;

public class Loops {

    public static void main(String[] args) {

        //For controlado por Contador

        for(int i=0;i<10;i++){

        }
        String[] names={"Sebastian","BR","C"};

        for(int i=0;i<names.length;i++){
            System.out.println(names[i]);
        }

        //foreach 

        for(String name:names){
            System.out.println(name);
        }

        HashSet<Integer> numbers=new HashSet<>();
        numbers.add(1);
        numbers.add(2);
        numbers.add(3);
        numbers.add(4);

        numbers.add(5);

        for (Integer number:numbers){
            System.out.println(number);
        }

        HashMap<String,Integer> clase=new HashMap<>();
        clase.put("Sebas", 10);
        clase.put("Lope", 7);
        clase.put("Desi", 9);
        
        for(Map.Entry<String,Integer> alumno:clase.entrySet()){
            System.out.println(alumno);

        }

        //While

        int i=0;
        while (i<10){
            System.out.println(i);
            i++;
        }
        i=0;
        while (i<names.length) {
            System.out.println(names[i]);
            i++;
        }

        boolean find=false;
        i=0;
        while (!find==true) {
            System.out.println(names[i]);
            if(names[i].equals("BR")){
                find=true;
            }
            i++;
        }

        //do while
        i=0;

        do{
            System.out.println("Hola compañeros");
            i++;

        }while(i<=0);
    }

}
