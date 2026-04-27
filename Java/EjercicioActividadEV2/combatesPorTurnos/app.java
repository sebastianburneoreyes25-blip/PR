package EjercicioActividadEV2.combatesPorTurnos;

import java.util.Scanner;

public class app {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Datos jugador 1
        System.out.print("Nombre del jugador 1: ");
        String nombre1 = sc.nextLine();

        System.out.print("Vida inicial jugador 1: ");
        int vida1 = sc.nextInt();
        sc.nextLine();

        System.out.print("Clase (Paladin/Picaro): ");
        String clase1 = sc.nextLine();

        // Datos jugador 2
        System.out.print("\nNombre del jugador 2: ");
        String nombre2 = sc.nextLine();

        System.out.print("Vida inicial jugador 2: ");
        int vida2 = sc.nextInt();
        sc.nextLine();

        System.out.print("Clase (Paladin/Picaro): ");
        String clase2 = sc.nextLine();

        // Crear personajes dinámicamente
        Personaje p1 = clase1.equalsIgnoreCase("Paladin")
                ? new Paladin(nombre1, vida1)
                : new Rogue(nombre1, vida1);

        Personaje p2 = clase2.equalsIgnoreCase("Paladin")
                ? new Paladin(nombre2, vida2)
                : new Rogue(nombre2, vida2);

        // Combate por turnos
        while (p1.estaVivo() && p2.estaVivo()) {

            // Turno jugador 1
            System.out.println("\nTurno de " + p1.nombre);
            turno(sc, p1, p2);

            if (!p2.estaVivo()) break;

            // Turno jugador 2
            System.out.println("\nTurno de " + p2.nombre);
            turno(sc, p2, p1);
        }

        // Resultado
        if (p1.estaVivo()) {
            System.out.println(p1.nombre + " gana!");
        } else {
            System.out.println(p2.nombre + " gana!");
        }

        sc.close();
    }

    public static void turno(Scanner sc, Personaje atacante, Personaje objetivo) {

        System.out.print("Tipo de ataque (normal/especial): ");
        String tipo = sc.nextLine();

        if (tipo.equalsIgnoreCase("especial") && atacante instanceof HabilidadEspecial) {
            ((HabilidadEspecial) atacante).activarEspecial(objetivo);
        } else {
            System.out.print("Daño a realizar: ");
            int dano = sc.nextInt();
            sc.nextLine();

            System.out.print("Usa armadura? (Escudo/ninguna): ");
            String armadura = sc.nextLine();

            if (armadura.equalsIgnoreCase("Escudo")) {
                objetivo.recibirDano(dano, armadura);
            } else {
                objetivo.recibirDano(dano);
            }
        }

        System.out.println(objetivo.nombre + " tiene " + objetivo.nombre + " de vida.");
    }
    }
    

