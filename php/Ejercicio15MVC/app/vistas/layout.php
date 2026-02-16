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
        <h1>Este MVC solo nos permitira borrar alumnos de la lista</h1>
        <a href="/Ejercicio15MVC/public/index.php?accion=listar">Ir a lista para borrar</a>
    </div>
    <?php if(!empty($contenidoVista)){
        require $contenidoVista;
    }
    ?>
</body>
</html>