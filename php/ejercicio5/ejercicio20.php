<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejercicio 20</title>
</head>
<body>
    <form action="ejercicio20.php" method="POST">
    <h3>Buscador de peliculas</h3>
    <label>Genero</label><br>
    <select name="genero" >
        <option value="Comedia">Comedia</option>
        <option value="Acción">Acción</option>
        <option value="Drama">Drama</option>
    </select>
    <input type="submit" value="Buscar">
    </form>

    <div style="display: flex; flex-wrap: wrap; gap: 15px;">

<div style="border: 2px solid #4A90E2; border-radius: 8px; padding: 15px; width: 200px; background-color: #f9f9f9; box-shadow: 2px 2px 5px rgba(0,0,0,0.1);"> <div style="font-weight: bold; font-size: 1.2em; margin-bottom: 8px;">Inception</div> <div style="font-style: italic; color: #555;">Ciencia Ficción</div> </div>

<div style="border: 2px solid #4A90E2; border-radius: 8px; padding: 15px; width: 200px; background-color: #f9f9f9; box-shadow: 2px 2px 5px rgba(0,0,0,0.1);"> <div style="font-weight: bold; font-size: 1.2em; margin-bottom: 8px;">The Godfather</div> <div style="font-style: italic; color: #555;">Drama / Crimen</div> </div>

<div style="border: 2px solid #4A90E2; border-radius: 8px; padding: 15px; width: 200px; background-color: #f9f9f9; box-shadow: 2px 2px 5px rgba(0,0,0,0.1);"> <div style="font-weight: bold; font-size: 1.2em; margin-bottom: 8px;">Spirited Away</div> <div style="font-style: italic; color: #555;">Animación / Fantasía</div> </div>

</div>
    <?php
    $seleccion=$_POST["genero"]??"";

    
    ?>
</body>
</html>