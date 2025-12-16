<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejercicio 1.4</title>
</head>

<body>
    <?php
    $respuestas = ["p1" => 'a', "p2" => 'b', "p3" => 'c', "p4" => 'c'];  //Diccionario con las respuestas
    //Variables
    $aciertos = 0;
    $cantidadPreguntas = count($respuestas);
    $mensaje = "";
    $respuestaCuestionario = "";
    //bucle para recorrer el diccionario de respuestas
    foreach ($respuestas as $pregunta => $respuestaCorrecta) {
        if ($_POST != null) {//solo si hay algo en el post entrara aqui.
            $respuestaCuestionario = $_POST[$pregunta] ?? "";//define la respuesta para liego compararla
            if ($respuestaCorrecta == $respuestaCuestionario) {//comparamos si la respuesta es correcta o no, si es correcta hara un sumatorio.
                $aciertos += 1;
        
            }
        }
    }

    $mensaje = "Has acertado $aciertos de $cantidadPreguntas";
    ?>
    <form action="ejercicio4.php" method="POST">
        <label>¿Cual fue el error de casi toda la clase en el examen de programación?</label><br><!--comentar :'( -->
        <input type="radio" name="p1" value="a" >Comentar el codigo <br>
        <input type="radio" name="p1" value="b">'<=''>=''+=' <br>
            <input type="radio" name="p1" value="c">No hubo fallos <br>
            <br>
            <label>¿Que clase nos da David?</label><br>
            <input type="radio" name="p2" value="a">Lenguaje de marcas <br>
            <input type="radio" name="p2" value="b">'Base de Datos<br>
            <input type="radio" name="p2" value="c">No tenemos ningun profesor<br>
            <br>
            <label>¿Que hemos aprendido en programacion?</label><br>
            <input type="radio" name="p3" value="a">Java<br>
            <input type="radio" name="p3" value="b">Angular<br>
            <input type="radio" name="p3" value="c">Python<br>
            <br>
            <label>¿Que hemos hecho en Base de Datos?</label><br>
            <input type="radio" name="p4" value="a">MongoDB<br>
            <input type="radio" name="p4" value="b">Cassandra<br>
            <input type="radio" name="p4" value="c">MySQL<br>
            <br>

            <input type="submit">
    </form>
    <?php echo $mensaje ?>
</body>

</html>