<?php
class Empleado{//definimos la clase padre empleado
    public $name;
    public $sueldo;
    public $anios_experiencia;
    public $bonus;

    public function calcular_bonus(){
        $multiplicador=floor($this->anios_experiencia/2);
        $bonus=$this->sueldo*(0.05*$multiplicador);

        echo"El bonus por ". $this->anios_experiencia ." años de experiencia es de $bonus €\n\n";
        return $bonus;
    }
    public function detalles(){
        echo "Nombre: ".$this->name. PHP_EOL;
        echo "Sueldo: ".$this->sueldo. PHP_EOL;
        echo "Años de experiencia: ".$this->anios_experiencia. PHP_EOL;
        echo "Bonus total: ".$this->bonus. PHP_EOL;
        $this->calcular_bonus(). PHP_EOL;
    }
}


?>