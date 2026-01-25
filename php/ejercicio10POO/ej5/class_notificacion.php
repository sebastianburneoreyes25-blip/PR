<?php

class Notificacion{

    private $mensaje;

    public function __construct($mensaje)
    {
        if(empty($mensaje)){
        throw new \Exception('Not implemented');}
        $this->mensaje=$mensaje;
    }
    

    public function enviar(){
        echo "Enviando $this->mensaje\n";
    }


}


?>