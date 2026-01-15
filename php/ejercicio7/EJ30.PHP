<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

    <?php 
    
    $fichero = "registros.txt";
    $log = "errores.log";
    $fechaActual = date("Y-m-d H:i:s");

    try {
        
        if (!file_exists($fichero)) {//Cuando no exista el fichero
            // Registramos el error antes de lanzar la excepción
            $msgError = "$fechaActual | EJ30 | No existe $fichero | " . basename(__FILE__) . " | línea " . (__LINE__ + 2) . PHP_EOL;
            file_put_contents($log, $msgError, FILE_APPEND);
            
            throw new Exception("No hay registros todavía.");
        }

        $registros = fopen($fichero, "r");
        
        echo "<table border=3>";
        echo "<tr>
                <th>Fecha y hora</th>
                <th>Nombre</th>
                <th>Email</th>
                <th>Edad</th>
                <th>Comentario</th>
              </tr>";

        $numLinea = 0;
       while (!feof($registros)) {
            $linea = fgets($registros);
            $numLinea++;
            $lineaLimpia = trim($linea);
            $lineaLimpia=str_replace(" ","",$lineaLimpia);

            // Solo procesamos si la línea no está vacía
            if ($lineaLimpia !== "") {
                $campos = explode('|', $lineaLimpia);

                // Verificamos si el formato es correcto (5 columnas)
                if (count($campos) === 5) {
                    echo "<tr>";
                    foreach ($campos as $campo) {
                        echo "<td>" . htmlspecialchars(trim($campo)) . "</td>";
                    }
                    echo "</tr>";
                } 
                else {
                    // Si el formato es incorrecto
                    $msgError = "$fechaActual | EJ30 | Línea $numLinea mal formateada | " . basename(__FILE__) . PHP_EOL;
                    file_put_contents($log, $msgError, FILE_APPEND);
                    
                    echo "<tr class='error-row'><td colspan='5'>Registro inválido en línea $numLinea (ver errores.log)</td></tr>";
                }
            }
        }

        echo "</table>";
        fclose($registros);

    } catch (Exception $e) {
        echo "<p style='color:red;'><strong>Aviso:</strong> " . $e->getMessage() . "</p>";
    }
    ?>

</body>
</html>

  