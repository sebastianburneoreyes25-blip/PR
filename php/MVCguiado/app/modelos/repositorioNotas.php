<?php
require_once __DIR__."/../notas.php";

class RepositorioNotas{
    private $path;


    function __construct()
    {
        $this->path=__DIR__."/../../storage/notas.txt";
    }

    function obtenerTodas(){
        if(!file_exists($this->path)){
            return [];
        }
        $notas=fopen($this->path, "r");
        while(!feof($notas)){
            $nota= Nota:: crearDesdeLinea($notas);
            $arrayNotas+=$nota;
        }
        return $arrayNotas;
    }

    
}


?>