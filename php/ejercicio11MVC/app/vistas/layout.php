<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>layout</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>

    <div class="contenedor">
        <h1>Gestor de Alumnos (MVC + PDO)</h1>
        <div class="menu">
            <a href="/ejercicio11MVC/public/index.php?accion=listar">Listar alumnos.</a>
            <a href="/ejercicio11MVC/public/index.php?accion=crear">Nuevo alumno</a>

        </div>
        <hr>
        <?php
        try{
        require $vistaContenido;
        }catch(Throwable $e){
            $log=__DIR__.'/../../storage/error.log';
            $fecha=date('Y-m-d H:i:s');

            $linea="[$fecha]|".$e->getMessage()."|".$e->getFile()."|". $e->getLine(). PHP_EOL;

            file_put_contents($log,$linea,FILE_APPEND); 
        }

        ?>
    </div>

</body>

</html>