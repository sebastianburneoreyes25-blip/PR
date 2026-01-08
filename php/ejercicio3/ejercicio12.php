<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejercicio 12</title>
</head>

<body>
    <h2>Escribe tu fecha de nacimiento</h2>
    <form action="ejercicio12.php" method="POST"><!--Aqui ira el "Formulario" donde introducira el dia de nacimiento-->
        <input type="date" name="fecha"><br>
        <input type="submit">
    </form>

    <?php
    //Varables a tener en cuenta
    $fecha = $_POST["fecha"] ?? "";
    $time = strtotime($fecha);//comvertimos un str en tiempo formato Unix
    $mensaje = "";
    $diasSemana = ["Monday" => "Lunes", "Tuesday" => "Martes", "Wednesday" => "Miercoles", "Thursday" => "Jueves", "Friday" => "Viernes", "Saturday" => "Sábado", "Saturday" => "Domingo"];
    
    if (isset($_POST["fecha"])) {
        
        $dia = date('l', $time);//Convierte el formato Unix de la fecha a un dia en ingles.
        foreach ($diasSemana as $day => $dias) {//El array sustituira en el mensaje el dia en ingles a español
            if ($dia == $day) {
                $mensaje = "<h2>Naciste el $dias.</h2>";
                
            }
            
        }
        echo ($mensaje);
    }


    ?>


</body>

</html>