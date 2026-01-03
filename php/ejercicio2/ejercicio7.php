<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejercicio 7</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>

<body>
    <form action="ejercicio7.php" method="POST" style="margin-left:2%;"><!--Formulario para tirar x cantidad de dados -->
        <label>Selecciona la cantidad de D6 a tirar:</label><br>
        <input type="number" min="0" name="dados"><br>
        <input type="submit">
    </form><br>
    <?php
    $cantidadD6 = (int)($_POST["dados"]) ?? 0;
    $total = 0;
    $visualDados = "";
    $resultadoDado = 0;

    if (isset($_POST["dados"])) {//solo si ha habido un post se mostrara los dados
        foreach (range(1, $cantidadD6) as $nDado) {//recorremos el bucle para crear visualmente los dados y darlos un valor
            $resultadoDado = rand(1, 6);//randomiza el numero a dar
            $total += $resultadoDado;//suma el total por cada ciclo
           //en visualdados crearemos un dado por cada ciclo expresando en el centro su resultado
            $visualDados = $visualDados . "<div style='width: 200px; margin-left:1%'>
        <div class='ratio ratio-1x1 border border-4 border-dark bg-info shadow'>
            <div class='d-flex justify-content-center align-items-center'>
                <span class='fs-1 fw-bold text-dark'>$resultadoDado</span>
            </div>   
        </div>
        </div><br>";
        }
    }
    echo ($visualDados);//mostramos los dados
    $mensajeFinal = "<h3>La suma total de los dados es $total</h3>";
    echo ($mensajeFinal);//mostramos el total
    ?>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>

</body>

</html>