<?php
require_once "class_reloj.php";

class Smartwatch extends Reloj{//Hereda de reloj
    private $sistemaOperativo;

    public function __construct($marca, $sistema){
        parent::__construct($marca);//usamos funcion padre
        $this->sistemaOperativo=$sistema;

    }
    public function detalles(){
        echo "Tengo un reloj de marca $this->marca con sistema operativo $this->sistemaOperativo.\n";
    }

}
?>