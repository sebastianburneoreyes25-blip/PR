<?php
require_once "class_estudiante.php";

try{
$estudiante1=new Estudiante("Julio", 48, "2º DAM" );//metemos datos
$estudiante1->detalles();
}catch (Throwable $e){
    $fecha = date("Y-m-d H:i:s");
    $msgError = "[$fecha] Error:" . $e->getMessage() . PHP_EOL;
    file_put_contents("error.log", $msgError, FILE_APPEND);
}

?>