<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejercicio 11</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>

    <h1 style="text-align: center;">Calculadora del IMC.</h1><!--Formulario para añadir el peso y la altura, cosas necesarias para calcular el IMC-->
    <form action="ejercicio11.php" method="POST">
        <label>Peso (KG)</label><br>
        <input type="number" step="0.1" min=0 name="peso"><br>
        <label>Altura (cm)</label><br>
        <input type="number" step="0.01" min=0 name="altura"><br>
        <input type="submit">
    </form>
    <?php
    $peso = $_POST["peso"] ?? 0;//variables a tener en cuenta
    $altura = $_POST["altura"] ?? 0;
    $mensaje = "";
    $class = "";
    if (isset($_POST["altura"])) {//solo si hay un post en memoria realizara el codigo siguiente
        $imc = $peso / ($altura ** 2);//calculamos el imc
        if ($imc < 18.5 && $imc > 0) {//dependiendo del imc dado seleccionara la clase y expresara el mensaje adecuado
            $class = "amarillo";
            $mensaje = "<h3 class='$class'>IMC=$imc Bajo peso</h3>";
        } elseif ($imc >= 18.5 && $imc <= 24.9) {
            $class = "verde";
            $mensaje = "<h3 class='$class'>IMC=$imc Peso normal</h3>";
        } elseif ($imc >= 25) {
            $class = "roja";
            $mensaje = "<h3 class='$class'>IMC=$imc Sobrepeso</h3>";
        }
        echo ($mensaje);
    }
    ?>
</body>

</html>