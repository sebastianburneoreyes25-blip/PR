public class condicionales {

    public static void main(String[] args) {
        int myAge = 18;

        if (myAge > 18) {
            System.out.println("Es mayor de edad");
        } else if (myAge == 18) {
            System.out.println("Justo tiene 18 años");
        } else {
            System.out.println("Es menor de edad");
        }

        int day=5;

        switch (day){
        case 1:
            System.out.println("Lunes");
            break;
        case 2:
            System.out.println("Martes");
            break;
        case 3:
            System.out.println("Miercoles");
            break;
        case 4:
            System.out.println("Jueves");
            break;
        case 5:
            System.out.println("Viernes");
            break;
        default:
            System.out.println("No entendi");
}

    /* Escribir un numero aleatorio entre 1 y 100 */
    int random=(int)(Math.random()*100)+1;
    System.out.println(random);

    /*Escribri un numero aleatorio entre 1 y 20 */

    random=(int)(Math.random()*20)+1;
    System.out.println(random);
    
    /*✅ 1. Sistema de registro de usuario
Crea un programa que:
 Declare las siguientes variables:
o String nombre
o int edad
o double estatura
o boolean esMayorDeEdad
 Imprima el tipo de dato de nombre usando getClass().getSimpleName().
 Determine si el usuario es mayor de edad (edad &gt;= 18) usando
operadores relacionales.
 Use un operador lógico &amp;&amp; para verificar si es mayor de edad y mide
más de 1.60.
 Muestre todos los resultados en consola. */
String name="Sebas";
int edad=26;
double estatura=1.75;
boolean esMayorDeEdad;
System.out.println("Tipo de dato usado en name:"+name.getClass().getSimpleName());

if(edad>=18){
     esMayorDeEdad=true;
}else{
     esMayorDeEdad=false;
}
System.out.println("Es mayor de edad: "+esMayorDeEdad);


if (esMayorDeEdad==true && estatura>=1.60){
    System.out.println("Es mayor de edad y mide más de 1.60 m");
}else{
    System.out.println("No es mayor de edad o no mide más de 1.60 m");
}

/*✅ 2. Calculadora básica con validación lógica
Crea un programa que:
 Declare dos variables int a y int b.
 Realice todas las operaciones aritméticas básicas (+, -, *, /, %).
 Use operadores de comparación para verificar:
o Si a es mayor que b
o Si ambos números son iguales
 Use operadores lógicos para verificar:
o Si a es mayor que 0 y b es mayor que 0.
 Use operadores de asignación compuesta (+=, *=, etc.) para modificar el
valor de a.
 Muestre cada resultado en pantalla. */

int a=5;
int b =10;

System.out.println(a+b);
System.out.println(a-b);
System.out.println(a*b);
System.out.println(a/b);
System.out.println(a%b);

if (a>b){
    System.out.println("a es mayor que b");
}else if(a==b){
    System.out.println("a es igual que b");
}

if(a>0&&b>0){
    System.out.println("a y b son mayores que 0");
}else{
    System.out.println("a o b no son mayores que 0");
}

a+=b;
System.out.println("a+=b =="+a);

/*✅ 3. Sistema de acceso con validación de correo
Crea un programa que:
 Declare una variable var email.
 Declare una constante final String EMAIL_ADMIN.
 Compare ambos correos usando operadores relacionales.
 Declare un boolean accesoPermitido.
 Use un operador lógico || para permitir acceso si:
o El correo coincide con el del administrador
o O si el usuario tiene más de 18 años.
 Imprima si el acceso fue concedido o denegado. */

String email="emial@email.email";
final String emailAdmin="ADMIN@ADMIN.ADMIN";

System.out.println(email==emailAdmin);

boolean accesoPermitido;
int userAge=18;

if(email==emailAdmin||userAge>=18){
    accesoPermitido=true;
    System.out.println("Acceso permitido: "+accesoPermitido);
}else{
    accesoPermitido=false;
    System.out.println("Acceso permitido: "+accesoPermitido);
}


/*✅ 4. Control de inventario con operadores unarios
Crea un programa que:
 Declare una variable int stock = 10;

 Simule:
o Una venta usando --stock
o Una reposición usando ++stock
 Use operadores de comparación para verificar si el stock es mayor que
0.
 Use operador lógico ! para verificar si NO está agotado.
 Muestre en pantalla cada cambio del stock y el resultado de las
evaluaciones lógicas. */


int stock=10;

--stock;
System.out.println(stock);
System.out.println(stock>0);
System.out.println("¿Hay stock? :"+(stock!=0));

/*✅ 5. Evaluación de notas de un estudiante
Crea un programa que:
 Declare tres variables int nota1, nota2, nota3.
 Calcule el promedio usando operadores aritméticos.
 Determine si el estudiante aprueba (promedio &gt;= 60).
 Use operador lógico &amp;&amp; para verificar si:
o El promedio es aprobatorio
o Y ninguna nota es menor que 50.
 Use operadores de asignación para incrementar una nota si está por
debajo de 50.
 Muestre todos los resultados en consola. */

int nota1=10;
int nota2=8;
int nota3=6;

double promedio=(nota1+nota2+nota3)/3;
System.out.println("Promedio "+promedio);
boolean aprobado;
if (promedio>=6){
    aprobado=true;
    System.out.println("El alumno ha aprobado: "+aprobado);
}else  {
    aprobado=false;
    System.out.println("El alumno ha aprobado: "+aprobado);

}

if(aprobado==true&&nota1>=5&&nota2>=5&&nota3>=5){
    System.out.println("Todos los requisitos pasados");
}else{
    System.out.println("No se ha pasado todos los requisitos");
}

    }

 

}
