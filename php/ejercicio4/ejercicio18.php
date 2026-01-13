<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejercicio 18</title>
</head>

<body>
    <form action="ejercicio18.php" method="POST"><!-- Pedimos los datos de las temperaturas-->
        <label>Temperatura día 1:</label><br>
        <input type="number" step="0.1" name="temperatura[]"><br>
        <label>Temperatura día 2:</label><br>
        <input type="number" step="0.1" name="temperatura[]"><br>
        <label>Temperatura día 3:</label><br>
        <input type="number" step="0.1" name="temperatura[]"><br>
        <label>Temperatura día 4:</label><br>
        <input type="number" step="0.1" name="temperatura[]"><br>
        <label>Temperatura día 5:</label><br>
        <input type="number" step="0.1" name="temperatura[]"><br>
        <input type="submit">
    </form>

    <?php
    $temperaturas = $_POST["temperatura"] ?? []; //guardamos el array de las temperaturas
    if (isset($_POST["temperatura"])) { //Si hay post de temperaturas, se realizara la definicion del maximo, minimo y su media.
        $tempMax = max($temperaturas);
        $tempMin = min($temperaturas);
        $media = array_sum($temperaturas) / count($temperaturas);
        echo ("<h3>La temperatura maxima fue $tempMax ºC. La temperatura minima fue $tempMin ºC. La media de los 5 días fue $media ºC.</h3>");
    };

    ?>

</body>

</html>