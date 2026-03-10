
public class Arrays {
    
    public static void main(String[] args) {
        
        //Declaracion y creacion
        int[] numbers=new int[3];//Defines la longitud que tendra
        System.out.println(numbers);

        String[] names={"Sebas", "BR"};
        System.out.println(names);

        //Acceso a arrays
        System.out.println(names[1]);
        System.out.println(names[0]);

        //modificar arrays
        
        numbers[0]=1;
        numbers[1]=10;
        System.out.println(numbers[0]);

    }



}
