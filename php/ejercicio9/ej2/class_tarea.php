<?php

class Tarea{//Definimos la clase con sus atributos y metodos.
    public $nombre;
    public $descripcion;
    public $fechaLimite;
    public $estado;

    public function marcarComoCompletada(){
        $this->estado="Completado";
        echo"Tarea completada \n";
    }
    public function editarDescripcion($descripcion){
        $this->descripcion=$descripcion;
        echo"Descripcion modificada correctamente \n";
    }
    public function mostrarTarea(){
        echo"Tarea:". $this->nombre. PHP_EOL;
        echo"Descripcion:". $this->descripcion. PHP_EOL;
        echo"Fecha limite:". $this->fechaLimite. PHP_EOL;
        echo"Estado:". $this->estado. PHP_EOL;
    }


}

?>