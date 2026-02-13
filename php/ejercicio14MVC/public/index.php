<?php
require_once __DIR__."/../app/controladores/ControladorAlumnos.php";

ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

$controlador=new ControladorAlumnos;

$accion=$_GET['accion']??'crear';//En caso que no tenga ningun modo, llevara a crear

switch($accion){
    case 'crear':
        $controlador->crear();
        break;
    case 'guardar':
        $controlador->guardar();
        break;
    case 'correcto':
        $controlador->correcto();
        break;
    default:
        echo "Accion no encontrada";
        break;
}



?>