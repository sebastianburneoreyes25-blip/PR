<?php
class Alumno{

    public $nombre;
    public $curso;

    public function __construct($nombre,$curso){//El constructor nos creara el objeto dependiendo de las variables dadas.

        $this->nombre=$nombre;
        $this->curso=$curso;
        
    }
    public function presentarse(){
        echo "Mi nombre es ". $this->nombre ." y estoy en el curso de ". $this->curso. PHP_EOL;
    }
}

?>