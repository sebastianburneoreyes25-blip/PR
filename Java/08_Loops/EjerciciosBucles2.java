package Java.Loops;

import java.lang.classfile.constantpool.IntegerEntry;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;

public class EjerciciosBucles2 {
    
    public static void main(String[] args) {
        
        //1. Crea un HashSet con 2 valores diferentes.
        HashSet<Integer> numbers=new HashSet<>();
        numbers.add(10);
        numbers.add(11);
        System.out.println(numbers);

        //2. Añade un nuevo valor repetido y otro sin repetir al HashSet.
        numbers.add(15);
        numbers.add(11);
        System.out.println(numbers);

        //3. Elimina uno de los elementos del HashSet.
        numbers.remove(11);
        System.out.println(numbers);
        //4. Crea un HashMap donde la clave sea un nombre y el valor el número de teléfono. Añade tres contactos.   
        HashMap<String,Integer> people=new HashMap<>();
        people.put("Sebas", 654789321);
        people.put("Lope", 654745621);
        people.put("Desi", 654897791);
        System.out.println(people);

        //5. Modifica uno de los contactos y elimina otro.
        people.put("Lope", 666666666);
        people.remove("Sebas");
        System.out.println(people);
        //6. Dado un Array, transfórmalo en un ArrayList, a continuación en un HashSet y finalmente en un HashMap con clave y valor iguales.
        String[] names={"Sebas","Lope","Ivam"};
        ArrayList<String> names2=new ArrayList<>(Arrays.asList(names));
        HashSet<String> names3=new HashSet<>(names2);
        HashMap<String,String> names4=new HashMap<>();
        for (int i=0;i<names2.size();i++){
            names4.put(names2.get(i),names2.get(i));
        }
        for (String name : names) {
            System.out.println(name);
        }
        System.out.println(names2);
        System.out.println(names3);
        System.out.println(names4);

        
        //7.-Imprime los números del 1 al 10 usando while.

        int contador=0;
        while (contador<10){
            contador++;
            System.out.println(contador);
        }
        //8 . Usa do-while para mostrar todos los valores de un ArrayList.
        contador=0;
        do{
            System.out.println(names[contador]);
            contador++;
        }while(contador<names.length);
        //9. Imprime los múltiplos de 5 del 1 al 50 usando for.
       
       for(int i=0;i<=50;i++){
        if(i%5==0){
            System.out.println(i);
        }
       }

        //10.  Recorre un Array de 5 números e imprime la suma total.
       int[] numbers2={1,5,8,9,10};
       int sumatorio=0;
       for (int i : numbers2) {
            sumatorio+=i;
       }
       System.out.println(sumatorio);

        //11. Usa un for para recorrer un Array y mostrar sus valores.
        for (int i : numbers2) {
            System.out.println(i);
       }
        //12. Usa for-each para recorrer un HashSet y un HashMap.
        HashMap<String,Integer> map1=new HashMap<>();
        map1.put("Sebas", 10);
        map1.put("Alex", 8);
        map1.put("Ivan", 10);
       for (Map.Entry<String,Integer> a:map1.entrySet()) {
        System.out.println(a);
       }

        HashSet<String> leters=new HashSet<>();
        leters.add("a");
        leters.add("b");
        leters.add("c");
        leters.add("d");
        leters.add("e");

        for (String a : leters) {
            System.out.println(a);
        }


        //13. Imprime los números del 10 al 1 (descendiente) con un bucle for.
        for(int i=10;i>0;i--){
            System.out.println(i);
        }

        //14. Usa continue para saltar los múltiplos de 3 del 1 al 20.
        for(int i=1;i<=20;i++){
            if(i%3==0){
                continue;
            }else{
                System.out.println(i);
            }
        }
        //15. Crea un programa que calcule el factorial de un número dado. 
        int numero=10;
        int resultado=1;
        for(int i=1;i<=numero;i++){
            resultado=resultado*i;

        }
        System.out.println(resultado);


    }
}
