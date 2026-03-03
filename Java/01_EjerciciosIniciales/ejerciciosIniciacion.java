
public class ejerciciosIniciacion {

    public static  void main (String[] args){   
    // 1. Declara una variable de tipo String y asígnale tu nombre.
        String myName="Sebas";
        System.out.println("1."+myName);
    // 2. Crea una variable de tipo int y asígnale tu edad.
        
        int myAge=26;
        System.out.println("2."+myAge);

    // 3. Crea una variable double con tu altura en metros.

        double myHeight=1.75;
        System.out.println("3."+myHeight+'m');

    // 4. Declara una variable de tipo boolean que indique si te gusta programar.

        boolean likePrograming=true;
        System.out.println("4. "+likePrograming);
    
    // 5. Declara una constante con tu email.

        final String email="email@mail.mail";
        System.out.println("5."+email);


    // 6. Crea una variable de tipo char y guárdale tu inicial.

        char inicial='S';
        System.err.println("6. "+inicial);


    // 7. Declara una variable de tipo String con tu localidad, y a continuación cambia su valor y vuelve a imprimirla.

        String localidad="Toledo";
        System.err.println("7.1. "+localidad);
        localidad="Madrid";
        System.err.println("7.2. "+localidad);
    // 8. Crea una variable int llamada a, otra b, e imprime la suma de ambas.

        int int1=5;
        int int2=9;
        System.out.println("8. "+(int1+int2));

    // 9. Imprime el tipo de dos variables creadas anteriormente.

        System.err.println("9. "+localidad.getClass().getSimpleName()+" "+myName.getClass().getSimpleName());

    // 10. Intenta declarar una variable sin inicializarla y luego asígnale un valor antes de imprimirla.

        int c;
        c=8;
        System.out.println("10. "+c);

        
    // 11.Crea una variable con el resultado de cada operación aritmética.

        int d=int1+int2;
        int e=int1-int2;
        int f=int1*int2;
        int g=int1/int2;
        int h=int1%int2;
        System.out.println("11.1 "+d);
        System.out.println("11.2 "+e);
        System.out.println("11.3 "+f);
        System.out.println("11.4 "+g);
        System.out.println("11.5 "+h);


    // 12. Crea una variable para cada tipo de operación de asignación.

        d=int1+int2;
        e=int1-int2;
        f=int1*int2;
        g=int1/int2;
        h=int1%int2;
        System.out.println("11.1 "+d);
        System.out.println("11.2 "+e);
        System.out.println("11.3 "+f);
        System.out.println("11.4 "+g);
        System.out.println("11.5 "+h);
        
        


    // 13. Imprime 3 comparaciones verdaderas con diferentes operadores de comparación.

        e=5;
        f=7;
        g=8;
        System.out.println("13. "+(e==5));
        System.out.println("13. "+(f!=5));
        System.out.println("13. "+(g>=5));
        

    // 14. Imprime 3 comparaciones falsas con diferentes operadores de comparación.

        System.out.println("14. "+(e<5));
        System.out.println("14. "+(e>5));
        System.out.println("14. "+(e==0));

    // 15. Utiliza el operador lógico and.

        System.out.println("15. "+(e==5 && f!=5));

    // 16. Utiliza el operador lógico or.

        System.out.println("16. "+(e==5 || f==5));
        

    // 17. Combina ambos operadores lógicos.

        System.out.println("17. "+(e==5 || f==5 && g>1));
        

    // 18. Añade alguna negación.

        System.out.println("18. "+(e==5 && f!=5));


    // 19. Imprime 3 ejemplos de uso de operadores unarios.

    System.out.println("19. "+ e++);

    // 20. Combina operadores aritméticos, de comparación y lógicos.

        System.out.println("20. "+(e+f>=5|| e==5));

    // Aritméticos

        var a = 5;
        var b = 3;

        System.out.println(a + b);
        System.out.println(a - b);
        System.out.println(a * b);
        System.out.println(a / b);
        System.out.println(a % b);



        // Asignación

        a = b;
        System.out.println(a);

        a = b * 2;
        System.out.println(a);

        a += 1; // a = a + 1
        System.out.println(a);

        a -= 1;
        System.out.println(a);
        a *= 2;
        System.out.println(a);
        a /= 2;
        System.out.println(a);
        a %= 2;
        System.out.println(a);


        // Comparación (Relacionales)

        System.out.println(a == b);
        System.out.println(a == 0);

        System.out.println(a != b);
        System.out.println(a > b);
        System.out.println(a >= b);
        System.out.println(a < b);
        System.out.println(a <= b);



        // Lógicos

        // Y (AND)
        System.out.println(true && true);
        System.out.println(true && false);
        System.out.println(false && true);
        System.out.println(false && false);

        System.out.println(3 > 2 && 5 == 2);

        // O (OR)
        System.out.println(true || true);
        System.out.println(true || false);
        System.out.println(false || true);
        System.out.println(false || false);

        System.out.println(3 > 2 || 5 == 2);

        // NO (NOT)
        System.out.println(!true);
        System.out.println(!false);

        System.out.println(!(3 > 2) || 5 == 2);



        // Unarios
        b=-10;
        System.out.println(+b);
        System.out.println(-b);
        System.out.println(++b);
        System.out.println(b++);
        System.out.println(b);
        System.out.println(--b);
        System.out.println(b--);
        System.out.println(b);
}
}