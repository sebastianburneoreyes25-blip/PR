package ejerciciosexepciones2;

public class array5 {

    public static void main(String[] args) {
        String[] s1=new String[3];

    try{
        System.out.println(s1[5]);
    }catch(ArrayIndexOutOfBoundsException e){
        System.out.println("Error: "+e.getMessage());
    }
    
    }
    
    
}
