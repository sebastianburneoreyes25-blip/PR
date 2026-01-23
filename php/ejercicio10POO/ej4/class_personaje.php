<?php

class Personaje{

    public $nombre;
    public $puntosVida;

    public function __construct($nombre,$puntosVida)
    {
        if(empty($nombre)){
        throw new \Exception('No hay nombre');
        } 
     if(empty($puntosVida)){
        throw new \Exception('No hay puntos de Vida');
        }
        $this->nombre=$nombre;
        $this->puntosVida=$puntosVida;
    }

}
?>