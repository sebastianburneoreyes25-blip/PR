<?php

class Reloj
{ //Creamos clase
    public $marca;

    public function __construct($marca)
    {
        if (empty($marca)) {
            throw new \Exception('Reloj sin marca.');
        }
        $this->marca = $marca;
    }
}
?>