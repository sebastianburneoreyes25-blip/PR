<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejercicio 6</title>
</head>

<body>
    <form action="ejercicio6.php" method="POST" style="margin-left: 5%;"><!--Creamos el formulario para que el usuario nos diga de que tamalano será la tabla -->
        <label>Cantidad de filas</label><br>
        <input type="number" min="0" name="filas"><br>
        <label>Cantidad Columnas</label><br>
        <input type="number" min="0" name="columnas"><br>
        <input type="submit">
    </form>
    <?php
    $cantidadFilas =(int) ($_POST["filas"] ?? 0); //recibimos la cantidad de filas
    $cantidadColumnas =(int) ($_POST["columnas"] ?? 0); //recibimos la cantidad de columnas
    //definimos variables a tener en cuentga para el bucle for
    $rows = 0;
    $columns = 0;
    $tr = "";
    $tabla = "<table border='3'>";
    if(isset($_POST["filas"])){//solo si hay post de filas se realizara las operaciones de creacion de tablas
    foreach (range(1,$cantidadFilas) as $f) { //recorremos el bucle empezando por la cantidad de filas
        $rows += 1;
        $tr = "<tr>"; //por cada fila se añadira a la variable tr el inicio de una fila de la tabla
        foreach (range(1,$cantidadColumnas) as $c) {
            $columns += 1;
            $tr = $tr . "<td>Fila $rows Columna $columns</td>"; //por cada coilumna se añadira a la fila un inicio y fin de columna con su texto incluido
        }
        $columns = 0;
        $tr = $tr . "</tr>"; //cerramos la fila
        $tabla = $tabla . $tr; //se añade a la tabla la fila
        $tr = ""; //se reinicia la variable tr para la siguiente fila
    }
    $tabla = $tabla . "</table>";
    echo ($tabla);
    }
    ?>
</body>

</html>