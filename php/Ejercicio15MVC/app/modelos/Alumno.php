<?php
class Alumno{//Solo se creara, nada mas

    public $id;
    public $nombre;
    public $email;
    public $edad;
    public $fecha_creacion;

    function __construct($id,$nombre,$email,$edad,$fecha){
        $this->id=$id;
        $this->nombre=$nombre;
        $this->email=$email;
        $this->edad=$edad;
        $this->fecha_creacion=$fecha;

    }

}


?>