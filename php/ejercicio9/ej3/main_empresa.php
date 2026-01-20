<?php
require_once "class_empleado.php";
require_once "class_consultor.php";


$empleado=new Empleado;
$empleado->name="Empleado 1";
$empleado->sueldo=1500;
$empleado->anios_experiencia=1;
$empleado->bonus=$empleado->calcular_bonus();
$empleado->detalles();

$consultor=new Consultor;
$consultor->name="Consultor";
$consultor->sueldo=1800;
$consultor->anios_experiencia=5;
$consultor->horas_proyecto=150;
$consultor->bonus=$consultor->calcular_bonus();
$consultor->detalles();


?>