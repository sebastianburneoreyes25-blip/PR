<?php

ini_set('display_errors', 1);//Controlamos errores
error_reporting(E_ALL);

require_once __DIR__. "\..\..\app\controladores\ControladorGuiado.php";

$controlador=new Controlador();

$accion=$_GET["accion"]??"listar";

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
    default:
        echo "Accion no valida";
    
}



?>