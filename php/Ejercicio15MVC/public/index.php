<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

require_once __DIR__."/../app/controladores/ControladorAlumno.php";


$controlador=new Controlador;

$accion=$_GET['accion']??'listar';

switch($accion){
    case 'listar':
        $controlador->listar();
        break;
    case 'borrar':
        $controlador->borrar();
        break;
    default:
        echo 'Accion no valida';
        break;
}


?>