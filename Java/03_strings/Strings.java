public class Strings {

    public static void main(String[] args) {
        
        String name="Sebas";

        var surname=new String("BR");

        System.out.println(name+" "+surname);

        //Obtener un caracter
        System.out.println(name.charAt(name.length()-1));

        //subcadena
        System.out.println(name.substring(2));
        System.out.println(name.substring(2,3));

        //Comprobar si contiene
        System.out.println(name.contains("as"));

        //comparacion
        System.out.println(name.equals("Sebas"));
        System.out.println(name.equalsIgnoreCase("Sebas"));

        //== vs .equals

        var a="Sebas";
        var b="Sebas";
        var c =new String("Sebas");
        System.out.println(a==c);
        System.out.println(a.equals(c));

        //trim

        System.out.println(" hola, buenos dias.".trim());

        //Format 
        int age =26;
        System.out.println(String.format("Soy %s y tengo %d", name, age));

    }

}
