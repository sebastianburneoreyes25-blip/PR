<?php

require_once "class_persona.php";

class Estudiante extends Persona{
    private $curso;

    public function __construct($name, $edad, $curso)
    {
        parent::__construct($name, $edad);//usamos funcion padre
        if(empty($curso)){
            throw new \Exception('Estudiante no creado. No hay curso'.PHP_EOL); 
        }
        $this->curso=$curso;
    }
    public function detalles(){
        parent::detalles();//usamos funcion padre
        echo " Curso: ". $this->curso . PHP_EOL;
    }
}

?>