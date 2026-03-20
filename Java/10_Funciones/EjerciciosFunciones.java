import java.util.ArrayList;

public class EjerciciosFunciones {

   
    public static void main(String[] args) {
        
        // 1. Crea una función que imprima "¡Te doy la bienvenida!".
        bienvenida();
        // 2. Escribe una función que reciba un nombre como parámetro y salude a esa persona.
        saludo("Sebas");
        // 3. Haz un método que reciba dos números enteros y devuelva su resta.
            int c= resta(5, 4);
            System.out.println(c);

        // 4. Crea un método que calcule el cuadrado de un número (n * n).
            c=cuadrado(8);
            System.out.println(c);
        // 5. Escribe una función que reciba un número y diga si es par o impar.
            String parImpar=parImpar(5);
            System.out.println(parImpar);
        // 6. Crea un método que reciba una edad y retorne true si es mayor de edad (y false en caso contrario).
            boolean esMayor;    
            esMayor= mayorMenorEdad(18);
            System.out.println(esMayor);
        // 7.  Crea una función que reciba una cadena y retorne su longitud.
            int longitud=longitud("Hola");
            System.out.println(longitud);

        //  8. Crea un método que reciba un array de enteros, calcula su media y lo retorna.
            ArrayList<Integer> enteros=new ArrayList<>();
            enteros.add(8);
            enteros.add(9);
            enteros.add(10);
            Integer media=mediaArrays(enteros);
            System.out.println(media);

        // 9. Escribe un método que reciba un número y retorna su factorial.
            int factorial=factorial(9);
            System.out.println(factorial);

        // 10. Crea una función que reciba un ArrayList<String> y lo recorra mostrando cada elemento.
        ArrayList<String> lista=new ArrayList<>();
        lista.add("Hola");
        lista.add("Hola");
        lista.add("Hola");
        lista.add("Hola");
        listar(lista);

    }
    //1
    public static void bienvenida(){
        System.out.println("¡Te doy la bienvenida !");
    }
    
    //2
    public static void saludo(String nombre){
        System.out.println(String.format("Hola %s", nombre));
    }
    
    //3
    public static int resta(int a, int b){
        int c=a-b;
        return c;
    }
    //4
    public static int cuadrado(int a){
        int c=a*a;

        return c;
    }
    //5
    public static String parImpar(int a){
       
       String b;
        
        if (a%2==0){
            b="Es par";
        }else{
            b="Es impar";
        }

        return b;
    }

    //6
    public static boolean mayorMenorEdad(int edad){
        boolean esMayor;
        if(edad<18){
            esMayor=false;
        }else{
            esMayor=true;
        }
        return esMayor;
    }

    //7
    public static int longitud(String palabra){
        int longitud=palabra.length();
        return longitud;
    }

    //8
    public static Integer mediaArrays(ArrayList<Integer> array){
        Integer suma=0;
        Integer media;
        for (Integer num : array) {
            suma+=num;
            
        }
        media=suma/array.size();
        return media;
    }

    //9
    public static int factorial(int a){
        int factorial=0;
        for(int i =0;i<a;i++ ){
            factorial+=i;
        }
        return factorial;
    }
    //10
    public static void listar(ArrayList<String> lista){
        for (String palabra : lista) {
            System.out.println(palabra);
            
        }
    }
}
