<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejercicio 2</title>
</head>
<?php

//Aqui definiremos las variables, todas y cada una de ellas iran con el _post que deben recibir del formulario.

$color = $_POST["color"] ?? "white";
$size = $_POST["size"]??"50";
$title = $_POST["title"]??"Tu título aquí";
$align = $_POST["align"]??"center";
//Se le asigna un varol predefinido para cuando cargue la pagina con el '?? "lo que quieras asignarle"'


?>

<body style="background-color:<?php echo $color ?>;"> <!-- Formulario para modificar la página -->

    <h1 style="font-size: <?php echo $size."px"?>; text-align:<?php echo $align?>"><?php echo $title ?></h1>

    <form action="ejercicio2.php" method="POST" style="text-align: center;">

        <label>Elige un color</label>
        <input type="color" name="color">
        <label>Selecciona el tamaño de la letra</label>
        <input type="range" name="size" min="5" max="100" step="5">
        <label>Texto del titulo</label>
        <input type="text" name="title">
        <label>Selecciona la alineacion del texto</label>
        <select name="align">
            <option value="right">Derecha</option>
            <option value="left">Izquierda</option>
            <option value="center">Centro</option>
        </select>
        <input type="submit" value="Enviar">



    </form>
</body>

</html>