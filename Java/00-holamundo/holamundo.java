public class holamundo{
    public static void main(String[] args){
        System.out.println("Hola");
        int myAge=37;
        System.out.println(myAge);
        byte myByte=127;//del -127 al 127
        double myDouble=5.888;//decimales con más de dos decimales
        char leter='A';//Solo para un caracter, se pone comilla simple siempre
        boolean myBolean=true;
        
        System.out.println(myBolean);
        System.out.println(myByte);
        System.out.println(leter);
        
        String myString="Hola buenos dias" ;//Siempre comillas dobles, String es una clase a diferncia del resto
        System.out.println(myString);

        //Tipo de dato en tiempo de ejecucion

        System.out.println(myString.getClass().getSimpleName());//El método getClass() en Java se utiliza para obtener la clase en tiempo de ejecución y getSimpleName()
        //  devuelve el nombre de la clase tal como aparece en el código fuente, omitiendo el nombre del paquete

        //Variables y constantes
        var email="sebastian@gmail,es";
         System.out.println(email);
        
        final String email2="Pues eso";
         System.out.println(email2);

            

    
     
    
    }


   
}

