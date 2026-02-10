<?php

class Curso
{
    public $id;
    public $nombre;
    public $horas;
    public $fecha_creacion;

    function __construct($id, $nombre, $horas, $fecha_creacion)
    {
        $this->id = $id;
        $this->nombre = $nombre;
        $this->horas = $horas;
        $this->fecha_creacion = $fecha_creacion;
    }
}
?>