import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public  class Main {


    public static void main(String[] args) {
        Main p=new Main();
        System.out.println("Ejecutando prog");
    }

   public List<String> process(List<String> a, Map<String, String> b, String c) {

    List<String> d = new ArrayList<>();

    for (String e : a) {

        if (b.get(e).equals(c) && e.length() > 10) {

            d.add(e);

        }

    }

    return d;

}

    
}



