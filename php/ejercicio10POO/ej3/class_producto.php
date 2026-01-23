<?php

class Producto{

    public $nombre;
    public $precio;

    public function __construct($nombre,$precio)
    {
        if(empty($nombre)){
        throw new \Exception('No hay nombre');
        } 
     if(empty($precio)){
        throw new \Exception('No hay precio');
        }
        $this->nombre=$nombre;
        $this->precio=$precio;
    }

}

?>