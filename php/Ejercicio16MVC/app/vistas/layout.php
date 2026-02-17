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
        <h1>Este MVC solo va a editar a partir de una lista dada</h1>
        <a href="/Ejercicio16MVC/public/index.php?accion=listar">Lista de alumnos</a>
    </div>

    <?php if(!empty($contenidoVista)){
        require $contenidoVista;
    }
    ?>
</body>
</html>