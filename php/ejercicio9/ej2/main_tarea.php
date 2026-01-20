<?php
require_once "class_tarea.php";

$tareas=[1=>"POO",2=>"Herencia", 3=>"Polimorfismo", 4=>"Encapsulamiento" ];//diccionario con los valores de las tareas
$listaTareas=[];//la lista de tareas se guardara aqui
foreach($tareas as $n=>$t){
$listaTareas[$n]=new Tarea;//bucle para crear la tarea automaticamente asi como la realizacion de sus metodos.
$listaTareas[$n]->nombre="Comprender $t";
$listaTareas[$n]->descripcion="Debemos comprender $t a objetos para ser buenos programadores";
$listaTareas[$n]->fechaLimite="2026-01-25 23:59";
$listaTareas[$n]->estado="No completado";

$listaTareas[$n]->mostrarTarea();
$descripcion="Debemos comprender la $t para ser buenos programadores, ya que a partir de ahora todo sera POO";
$listaTareas[$n]->editarDescripcion($descripcion);
$listaTareas[$n]->marcarComoCompletada();
$listaTareas[$n]->mostrarTarea();
echo"\n\n\n";
}

?>