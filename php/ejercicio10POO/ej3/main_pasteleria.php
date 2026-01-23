<?php

require_once "class_pastel.php";
try {
    $donut = new Pastel("Donut", 15.5, "chocolate");
    $donut->detalles();
} catch (Throwable $e) {
    $fecha = date("Y-m-d H:i:s");
    $msgError = "[$fecha] Error: " . $e->getMessage() . PHP_EOL;
    file_put_contents("error.log", $msgError, FILE_APPEND);
}
?>