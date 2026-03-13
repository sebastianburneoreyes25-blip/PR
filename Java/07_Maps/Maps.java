import java.util.HashMap;

public class Maps {

    public static void main(String[] args) {
        
        HashMap<String, Integer> mapExample=new HashMap<>();
        var numbers= new HashMap<Integer,String>();

        //Tamaño
        System.out.println(mapExample.size());
        
        //Inserción
        mapExample.put("Sebas", 10);
        System.out.println(mapExample.size());
        System.out.println(mapExample);

        //Acceso
        System.out.println(mapExample.get("Sebas"));

        //Busqeuda 
        System.out.println(mapExample.containsKey("SeBAS"));
        System.out.println(mapExample.containsValue(8));

        //Eliminar
        mapExample.remove("Sebas");
        System.out.println(mapExample);
        mapExample.put("Sebas", 100);

        //Limpiar estructura
        System.out.println(mapExample);
        mapExample.clear();
        System.out.println(mapExample);

        //Modificacaion
        mapExample.put("Sebas", 100);
        System.out.println(mapExample);

        mapExample.put("Sebas", 1000);
        System.out.println(mapExample);

        mapExample.replace("Sebas", 1);
        System.out.println(mapExample);

        mapExample.putIfAbsent("BR", 11);

        /*Otras operaciones */
        System.out.println(mapExample.isEmpty());
        
    }


    
}
