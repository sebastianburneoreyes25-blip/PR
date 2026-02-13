<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>
    <div class="contenedor">
        <h1>Crear Alumno (CREATE con PDO)</h1>

        <p>Esta web solo permite insertar alumnos en la base de datos.</p>

        <hr>

        <?php
        if (!empty($contenidoVista)) {
            require $contenidoVista;
        }
        ?>
        <form action="/ejercicio14MVC/public/index.php?accion=crear">
            <input type="submit" value="Crear">
        </form>
    </div>

</body>

</html>