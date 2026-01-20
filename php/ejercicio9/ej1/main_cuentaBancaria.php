<?php
require_once("class_cuentaBancaria.php");

$miCuenta=new CuentaBancaria;
$miCuenta->titular="Sebastian Burneo";
$miCuenta->tipoDeCuenta="Cuenta joven";
$miCuenta->saldo=3000;

$miCuenta->consultarDatos();
$miCuenta->retirar(500);
$miCuenta->consultarDatos();
$miCuenta->depositar(800);
$miCuenta->consultarDatos();

?>