<?php 

require_once "class_carrito.php";

//realizamos acciones con las funciones de la clase Carrito
$miCarro=new Carrito;
$miCarro->agregarProcuto("producto 1", 15, 5);
$miCarro->agregarProcuto("producto 2", 15, 5);
$miCarro->mostrarDetalle();
$total=$miCarro->calcularTotal();
$miCarro->quitarProducto("producto 1");
$miCarro->mostrarDetalle();


?>