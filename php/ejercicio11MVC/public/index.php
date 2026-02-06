<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

require_once __DIR__."/../app/controladores/ControladorAlumnos.php";

$controlador =new ControladorAlumnos;

$accion=$_GET['accion']??'listar';

switch($accion){

    case 'listar':
        $controlador->listar();
        break;
    case 'crear':
        $controlador->crear();
        break;
    case 'guardar':
        $controlador->guardar();
        break;
    case 'borrar':
        $controlador->borrar();
        break;
    default:
        echo 'Acción no válida';
}



?>