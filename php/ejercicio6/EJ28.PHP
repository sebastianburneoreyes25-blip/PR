<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>

    <?php
    $mensaje = "";
    if ($_SERVER["REQUEST_METHOD"] == "POST") { //si hay post hara esto
        $accion = $_POST["accion"] ?? "";
        $archivo = "tareas.txt";
        $listar = "";
        if ($accion == "Añadir Tarea") {
            $añadir = "
        <label>Dia y hora de la tarea.</label><br>
        <input type='datetime-local' name='fecha'><br>
        <label>Descripcion breve</label><br>
        <input type='text' name='descripcion'><br>"; //formulario para guaradar el dia hora y tarea a realizar. Se añadira solamente si se da a añadir tarea.
            if (isset($_POST["fecha"])) {
                $fecha = $_POST["fecha"] ?? "";
                $descripcionTarea = $_POST["descripcion"] ?? "";
                $tarea = "$fecha || $descripcionTarea" . PHP_EOL;
                file_put_contents($archivo, $tarea, FILE_APPEND); //agregamos a archivo la tarea
                echo ("<h2 style='color:green'>Tarea guardada correctamente</h2>");
            }
        } elseif ($accion == "Listar tareas") {
            try {
                if (!file_exists($archivo)) {
                    echo ("No hay tareas todavia");
                    $archivo = fopen($archivo, "w"); //se crea archivo si no existe
                    fclose($archivo);
                }
                if (filesize($archivo) == 0) {
                    throw new Exception("El archivo $archivo esá vacío"); //Si esta vacia la lista, guaradara el error
                }
                $listaTareas = fopen($archivo, "r");
                $listar = "<ul>";
                while (!feof($listaTareas)) {
                    $tarea = fgets($listaTareas);
                    if (trim($tarea) != "") { //evitamos listar lineas vacias
                        $listar = $listar . "<li>$tarea</li>";
                    }
                }
            } catch (Exception $e) {
                $fecha = date("Y-m-d H:i:s");
                $error = "[$fecha]ERROR:" . $e->getMessage() . PHP_EOL; //mensaje que se guaradara en el error.log
                file_put_contents("error.log", $error . FILE_APPEND);
            }
        } elseif ($accion == "Salir") {
        }
    }
    ?>

    <form action="EJ28.PHP" method="POST">
        <?php
        if ($accion == "Añadir Tarea") {
            echo ($añadir);
        }
        ?>

        <input type="submit" value="Añadir Tarea" name="accion"><br>
        <input type="submit" value="Listar tareas" name="accion"><br>
        <input type="submit" value="Salir" name="accion"><br>

        <?php
        if ($accion == "Listar tareas") {
            echo ($listar);
        }
        ?>
    </form>

</body>

</html>