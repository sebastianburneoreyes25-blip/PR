<?php

require_once "class_smartwatch.php";
try {
    $samsungW5 = new Smartwatch("Samsung", "Android");
    $samsungW5->detalles();
} catch (Throwable $e) {
    $fecha = date("Y-m-d H:i:s");
    $msgError = "[$fecha] Error: " . $e->getMessage() . PHP_EOL;
    file_put_contents("error.log", $msgError, FILE_APPEND);
}
?>