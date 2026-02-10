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
        <h1>Alumnos (READ con PDO)</h1>
        <p>Esta weeb solo lee alumnos de la base de datos</p>
        <?php if (!empty($contenidoVista)) {//solo la pide si no esta vacio
            require $contenidoVista;
        } ?>
        <form action="/ejercicio13MVC//public/index.php?accion=listar">
            <input type="submit" value="Listar ahora">
        </form>
    </div>
</body>

</html>