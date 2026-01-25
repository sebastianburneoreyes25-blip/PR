<?php
require_once "class_notificacion.php";


class Email extends Notificacion{

    private $destinatario;

    public function __construct($mensaje, $destinatario)
    {
        parent::__construct($mensaje);
         if (empty($destinatario)){
            throw new Exception("No hay destinatario");
        }
        $this->destinatario=$destinatario;

    }

    public function enviar(){
        echo "Para : $this->destinatario \n";
        parent::enviar();
    }
}

?>