<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejercicio 12</title>
</head>

<body>
    <h2>Escribe tu fecha de nacimiento</h2>
    <form action="ejercicio12.php" method="POST">
        <input type="date" name="fecha"><br>
        <input type="submit">
    </form>

    <?php
    $fecha = $_POST["fecha"] ?? "";
    $time = strtotime($fecha);
    $mensaje = "";
    $diasSemana = ["Monday" => "Lunes", "Tuesday" => "Martes", "Wednesday" => "Miercoles", "Thursday" => "Jueves", "Friday" => "Viernes", "Saturday" => "Sábado", "Saturday" => "Domingo"];
    
    if (isset($_POST["fecha"])) {
        //$flag=false;
        $dia = date('l', $time);
        foreach ($diasSemana as $day => $dias) {
            if ($dia == $day/* and $flag=false*/) {
                $mensaje = "<h2>Naciste el $dias.</h2>";
                //$flag=true;
            }
            
        }
        echo ($mensaje);
    }


    ?>


</body>

</html>