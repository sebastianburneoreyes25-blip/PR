<?php

class CocheF1{
    public $piloto;
    public $velocidad=0;//definimos automaticamente la velocidad de inicio

    public function __construct($nombre){
        if(empty($nombre)){
        throw new \Exception('Piloto no creado. Falta el nombre');
        } 
        $this->piloto=$nombre;
    }
    public function acelerar(){
        $this->velocidad+=20;
        echo "Velocidad aumentada en 20Km/h. Velocidad acutal:". $this->velocidad. PHP_EOL;
        
    }
    

}

?>