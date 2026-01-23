<?php
require_once "class_empleado.php";
try {
    $becario = new Empleado("Luis", "Becario", 600);
    $becario->revisarSalario();
    $becario->revisarSalario();//Hacemos doble comprobacion, en uno actualiza y en otro comprobara si es suficiente.

    $jefa = new Empleado("Marta", "Jefa", 2500);
    $jefa->revisarSalario();
} catch (Throwable $e) {
    $fecha = date("Y-m-d H:i:s");
    $msgError = "[$fecha] Error:" . $e->getMessage() . PHP_EOL;
    file_put_contents("error.log", $msgError, FILE_APPEND);
}
?>