<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejercicio 14</title>
</head>

<body>
    <form action="ejercicio14.php" method="POST"><!--Formulario del dinero a cambiar -->
        <h2>¿De cuanto dinero quieres el cambio?</h2>
        <input type="number" name="dinero" min="0"><br>
        <input type="submit">
    </form>

    <?php
    //Variables a tener en cuenta
    $dinero = $_POST["dinero"] ?? 0;
    $cambio = [50 => 0, 20 => 0, 10 => 0, 5 => 0, 2 => 0, 1 => 0];
    $resto = 1;

    if (isset($_POST["dinero"])) { //Si se ha enviado el formulario empezara a ejecutar el calcular el cambio
        foreach ($cambio as $valor => $cantidad) {
            if ($dinero >= $valor and $resto != 0) {
                $cantidad = floor($dinero / $valor); //la cantidad de el valor sera la division entera del dinero que haya/quede por cambiar y el valor monetario
                $resto = $dinero % $valor;
                $dinero = $resto;
            };
            if ($valor > 2) {
                echo ("<p>$cantidad billetes de $valor €</p><br>");
            } else {
                echo ("<p>$cantidad monedas de $valor €</p><br>");
            }
        }
    }
    ?>

</body>

</html>