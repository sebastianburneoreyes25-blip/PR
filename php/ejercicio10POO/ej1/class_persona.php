<?php

class Persona{
    private $name;
    private $edad;

    public function __construct($name,$edad){
        if(empty($name)){
        throw new \Exception('No creada. No hay nombre'.PHP_EOL);
        }
        if(empty($edad)){
        throw new \Exception('No creada. No hay edad'.PHP_EOL);
        }
        $this->name=$name;
        $this->edad=$edad;
    }
    public function detalles(){
        
        echo $this->name. " ". $this->edad." años";
    }

}

?>