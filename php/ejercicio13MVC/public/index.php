<?php 

ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

require_once __DIR__."/../app/controlador/ControladorAlumnos.php";

$controlador=new Controlador;

$accion=$_GET['accion'] ?? 'listar';

switch($accion){
    case 'listar':
        $controlador->listar();
        break;
    default:
    echo 'Accion no válida';
}


?>