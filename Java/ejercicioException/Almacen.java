import java.util.Scanner;

public class Almacen {
    


    public static void main(String[] args) {
        
        String[] productos=new String[3];
        int i;
        Scanner sc = new Scanner(System.in);
        String prodName;

       
        try{
             System.out.println("Escribe el numero del produto a añadir(0-2)");
             i=sc.nextInt();
            System.out.println("Dame el nombre del producto a añadir");
            sc.nextLine();
            prodName=sc.nextLine();
            productos[i]=prodName;
            if ( productos[i].trim().isEmpty()) {
                throw new NullPointerException();
            }
            System.out.println("El producto se ha añadido correctamente ");
            
            System.out.println("Largo del nombre del producto :"+productos[i].length());


        }catch (ArrayIndexOutOfBoundsException e){
            System.out.println("El indice para el producto dado no esta en rango. Error: "+e.getMessage());

        
        }catch(NullPointerException e){
            System.out.println("Posicion vacia. Eroor: "+e.getMessage());

        }catch (Exception e){
            System.out.println("Error inesperado: "+e.getMessage());}
        finally{
            System.out.println("Estado del inventario actualizado");
            sc.close();
        }
        
       

        

    }
}
