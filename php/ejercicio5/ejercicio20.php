<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejercicio 20</title>
</head>
<body>
    <form action="ejercicio20.php">
    <h3>Buscador de peliculas</h3>
    <label>Genero</label><br>
    <select name="genero" >
        <option value="Comedia">Comedia</option>
        <option value="Acción">Acción</option>
        <option value="Drama">Drama</option>
    </select>
    <input type="submit" value="Buscar">
    </form>

    <?php
    $seleccion=$_POST["genero"]??"";
    
    ?>
</body>
</html>