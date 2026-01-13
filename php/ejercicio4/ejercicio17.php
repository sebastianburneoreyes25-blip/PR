<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejercicio 17</title>
</head>

<body>
    <form action="ejercicio17.php" method="POST" style="text-align: center;"><!--Pedimos la altura de la piramide-->
        <h1>Creador de piramides</h1>
        <label>Altura</label><br>
        <input type="number" name="altura"><br>
        <input type="submit">
    </form>
    <?php
    $altura = $_POST["altura"] ?? 0;
    $lineaPiramide = "";
    if (isset($_POST["altura"])) {
        foreach (range(0, $altura) as $i) { //en el rango dado se ira creando linea a linea la piramide.
            $lineaPiramide = ""; //limpia la linea que se expresara
            foreach (range(0, $i) as $e) {
                $lineaPiramide = $lineaPiramide . "*"; //añade un * por cada bucle
            };
            echo ("<p style='text-align: center;'>$lineaPiramide</p>"); //expresa la linea creada de la piramide con *.

        }
    }
    ?>
</body>

</html>