<?php

require_once "class_empleado.php";

class Consultor extends Empleado
{ //Hereda atributos y metodos del padre Empleado

    public $horas_proyecto; //añadimos las horas en el proyecto

    public function calcular_bonus()
    { //redefinimos funcion

        $bonus = parent::calcular_bonus(); //calculamos el bonus por años usando la funcion padre 

        if ($this->horas_proyecto >= 100) { //si tiene mas de 100h añade un bonus extra
            $bonus += 500;
            echo "+500€ por horas trabajadas en proyecto";
        }
        return $bonus;
    }
}
