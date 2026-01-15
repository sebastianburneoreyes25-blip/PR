<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>


    <?php
    try {
        if (!file_exists("usuarios.txt")) { //Si no existe lanzara el error
            throw new Exception("No existe el archivo usuarios.txt");
        }
        if (filesize("usuarios.txt") == 0) { //si el archivo esta vacio, tambien lanzara el mensaje de error
            throw new Exception("El archivo usuarios.txt esta vacío");
        }
        $usuarios = fopen("usuarios.txt", "r"); //carga  la lista de usuarios en la variable
        echo ("<h2>lista de usuarios</h2>");
        echo ("<ul>");
        while (!feof($usuarios)) { //hasta que acabe el archivo seguira el bucle while recorriendo linea por linea
            $li = fgets($usuarios);
            if (trim($li) != "") { //evitamos con el trim que lea lineas vacias
                echo ("<li>$li</li>");
            }
        }
        echo ("</ul>");
        fclose($usuarios);
    } catch (Exception $e) {
        $fecha = date("Y-m-d H:i:s");
        $mensajeError = "$fecha Error:" . $e->getMessage() . PHP_EOL; //si falla, guardamos el mensaje con la fecha y enviamos a error.log
        file_put_contents("error.log", $mensajeError, FILE_APPEND);
        echo ("<h2>ERROR</h2>");
    }

    ?>
</body>

</html>