<?php

require_once "class_personaje.php";

class Guerrero extends Personaje{
    public $arma;

    public function detalles(){
    echo "$this->nombre, $this->puntosVida HP. Arma:$this->arma";
    }
}


?>