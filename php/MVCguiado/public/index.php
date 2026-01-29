<?php

ini_set('display_errors', 1);//Controlamos errores
error_reporting(E_ALL);

require_once __DIR__. "\..\..\MVCguiado\app\controladores\ControladorGuiado.php";

$controlador=new Controlador();//creamos objeto para usar sus metodos

$accion=$_GET["accion"]??"listar";//cogera la accion de la url

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
        break;
    
}



?>