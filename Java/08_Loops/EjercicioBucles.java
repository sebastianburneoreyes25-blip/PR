

import java.util.Scanner;

public class EjercicioBucles {
    
/*Desarrolla un programa en Java que:
Genere un número aleatorio entre 1 y 20 (ambos incluidos).
Solicite al usuario que introduzca un número para intentar adivinarlo.
Permita seguir introduciendo números hasta que lo adivine (utilizando un bucle).
En cada intento, el programa deberá indicar:
“El número secreto es mayor”
o “El número secreto es menor”
Cuando el usuario acierte, el programa mostrará:
Un mensaje de felicitación.
El número total de intentos realizados.*/

public static void main(String[] args) {
    int secretNumber=(int)(Math.random()*20)+1;
    System.out.println("Adivina el número entre el 1 al 20");
    Scanner sc=new Scanner(System.in);
    System.out.println("Introduce el numero que crees que es.");
    int userNumber=sc.nextInt();
    int contador=1;
    while (userNumber!=secretNumber) {
        if (userNumber>secretNumber) {
            System.out.println("El numero secreto es menor");
        }else{
            System.out.println("El numero secreto es mayor");
        }
        userNumber=sc.nextInt();
        contador++;

    }
    sc.close();
    System.out.println(String.format("Correcto!!! Adivinado en %d intentos",contador));

}

}
