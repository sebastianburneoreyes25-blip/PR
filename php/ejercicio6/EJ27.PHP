<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <?php
    $palabra = "PHP"; //Variables a buscar y archivop
    $archivo = "texto.txt";

    try {
        if (!file_exists($archivo)) { //Si no existe lanzara el error
            throw new Exception("El archivo $archivo no existe");
        }
        if (filesize($archivo) == 0) { //si el archivo esta vacio, tambien lanzara el mensaje de error
            throw new Exception("El archivo $archivo esta vacío");
        }
        $texto = file_get_contents($archivo);
        $conteo = substr_count(strtolower($texto), strtolower($palabra)); //con el strtoloweer convertira los str a minusculas para que no varie por eso el resultado
        echo ("<h2>La palabra $palabra aparece $conteo veces en el texto.");
    } catch (Exception $e) {
        $fecha = date("Y-m-d H:i:s");
        $mensaje = "[$fecha] ERROR:" . $e->getMessage() . PHP_EOL;
        file_put_contents("error.log", $mensaje, FILE_APPEND); //envio mensaje de error
    }

    ?>


</body>

</html>