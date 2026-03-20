public class Funciones {


    public static void main(String[] args) {
        hola();


    }
    //Funciones sin parametros ni retorno
    public static void hola(){
        System.out.println("Hola mundo");
    }
    //Funciones con parametros
    public static void holaPersona(String persona){
        System.out.println(String.format("Hola %s",persona));
    }
    //Sobrecarga de funcion(mas de un parametro)
    public static void holaGRUPO(String persona, Integer edad){
        System.out.println(String.format("Hola %s, ¿tienes %d años?", persona,edad));
    }

    //funciones con retorno
    public static boolean/*valor que devolvera */ validacion(boolean valido){
        valido=false;
        return valido;
    }
    
}
