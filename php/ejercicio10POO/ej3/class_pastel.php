<?php

require_once "class_producto.php";

class Pastel extends Producto{//Hereda de producto
    public $sabor;

    public function __construct($nombre, $precio, $sabor)
    {
        parent::__construct($nombre, $precio);
        if(empty($sabor)){
        throw new \Exception('No hay sabor');
        }
        $this->sabor=$sabor;

    }
    public function detalles(){
        echo "Pastel de $this->sabor: $this->nombre - $this->precio euros";

        }
}
?>