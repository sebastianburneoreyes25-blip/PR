<?php

class Empleado
{
    private $nombre;
    private $puesto;
    private $sueldo;

    public function __construct($nombre, $puesto, $sueldo)
    {
        //Se crea una excepcion especifica para cada atributo de la clase, asi concretamos más correctamente el fallo.
        if (empty($nombre)) {
            echo "No puede haber empleado sin nombre, empleado no creado. \n";
            throw new \Exception('Empleado no creado, falta nombre' . PHP_EOL);
        }
        if (empty($puesto)) {
            echo "No puede haber empleado sin puesto, empleado no creado. \n";
            throw new \Exception('Empleado no creado, falta puesto' . PHP_EOL);
        }
        if (empty($sueldo)) {
            echo "No puede haber empleado sin sueldo, empleado no creado. \n";
            throw new \Exception('Empleadoo creado, falta sueldo' . PHP_EOL);
        }

        $this->nombre = $nombre;
        $this->puesto = $puesto;
        $this->sueldo = $sueldo;
        echo "Empleado creado correctamente. \n";
    }
    public function revisarSalario()
    {
        if ($this->sueldo < 1000) {//hasta no ser 1000 minimo el salario, no parara de incrementar
            while ($this->sueldo < 1000) {
                $this->sueldo += 200;
            }
            echo "Salario de actualizado.\n";
        } else {
            echo "Salario correcto.\n";
        }
    }
}
