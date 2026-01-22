<?php

require_once "class_personaje.php";


//Creacion de personajes
$guerrero = new Personaje();
$guerrero->nombre = "Guerrero";
$guerrero->nivel = 1;
$guerrero->puntosVida = 100;
$guerrero->puntosAtaque = 15;

$mago = new Personaje();
$mago->nombre = "Mago";
$mago->nivel = 1;
$mago->puntosVida = 70;
$mago->puntosAtaque = 20;

$arquero = new Personaje();
$arquero->nombre = "Arquero";
$arquero->nivel = 1;
$arquero->puntosVida = 80;
$arquero->puntosAtaque = 12;

//Simulacion de batalla

echo "¡Comienza la batalla!\n\n";

$guerrero->ataque($mago);
$mago->ataque($guerrero);

$arquero->ataque($mago);

$mago->curarse();

$guerrero->ataque($mago);

$arquero->subir_nivel();
$arquero->ataque($guerrero);

$guerrero->curarse();

echo "¡Fin de la batalla!\n";

?>