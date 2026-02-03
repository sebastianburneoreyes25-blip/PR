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
        require $vistaContenido;
        ?>
    </div>

</body>

</html>