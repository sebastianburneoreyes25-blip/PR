<?php

class Producto{//clase producto donde se creara automaticamente con el precio sin Iva
    public $descripcion;
    public $precioSinIva;

    public function __construct($descripcion, $precioSinIva){
        $this->descripcion=$descripcion;
        $this->precioSinIva=$precioSinIva;
        
    }
    public function calcularPrecio(){
        $precioIva=($this->precioSinIva*1.21);
        echo "El precio del producto es $precioIva IVA incluido.\n";
    }
}

?>