<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Añadir contacto</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>
    <div class="container">
        <form action="add_contacto.php" method="POST">
            <label>Nombre y apellidos</label><br>
            <input type="text" name="nombre"><br>
            <label>Télefono</label><br>
            <input type="number" name="telefono" min="0"><br>
            <input type="submit" value="Añadir" class="btn"><br>
        </form>
        <form action="index.php">
            <input type="submit" value="Volver a menu" class="btn"><br>
        </form>
        <?php
        function comprobarNombre($name)//funciones de comprobacion
        {
            if (trim($name) == "") {
                echo ("<h2>El nombre no debe estar vacío</h2>");
                throw new Exception("El nombre no puede estar vacío");
            }
        }
        function comprobarNumero($tel)
        {
            if (trim($tel) == "") {
                echo ("<h2>El teléfono no puede estar vacío</h2>");
                throw new Exception("Debe haber número de télefono");
            }
        }


        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            $telefono = $_POST["telefono"] ?? "";
            $nombre = $_POST["nombre"] ?? "";
            $archivo = "agenda.txt";
            if (isset($_POST["telefono"])) {
                try {
                    comprobarNombre($nombre);
                    comprobarNumero($telefono);
                    $msg = "$nombre|$telefono". PHP_EOL;//agrega el contacto a la agenda con este formato separados por '|'
                    file_put_contents($archivo, $msg, FILE_APPEND);
                    echo ("<h2> El contacto se ha guardado correctamente");
                } catch (Exception $e) {
                    $fecha = date("Y-m-d H:i:s");
                    $msgError = "[$fecha] Error:" . $e->getMessage() . PHP_EOL;
                    file_put_contents("error.log", $msgError, FILE_APPEND);
                }
            }
        }
        ?>

    </div>
</body>

</html>