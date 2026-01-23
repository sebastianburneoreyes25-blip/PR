<?php
require_once "class_cocheF1.php";


try{
$alonsoCoche=new CocheF1("Alonso");
$alonsoCoche->acelerar();
$alonsoCoche->acelerar();
$alonsoCoche->acelerar();
$alonsoCoche->acelerar();
$alonsoCoche->acelerar();


} catch(Throwable $e){
$fecha = date("Y-m-d H:i:s");
    $msgError = "[$fecha] Error:" . $e->getMessage() . PHP_EOL;
    file_put_contents("error.log", $msgError, FILE_APPEND);
}

?>