<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <form action="EJ29.PHP" method="POST"><!-- Formulario html con metodo post-->
        <label>Nombre</label><br>
        <input type="text" name="nombre"><br>
        <label>Email</label><br>
        <input type="mail" name="mail"><br>
        <label>Edad</label><br>
        <input type="number" min="0" max="120" step="1" name="edad"><br>
        <label>Comentario</label><br>
        <textarea name="comentario" maxlength="200" placeholder="Escribe aquí..."></textarea><br>
        <input type="submit">
    </form>

    <?php
    function validarEmail($email)//funcion para validar el mail automaticamente, con su throw en caso de que no sea valido
    {
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            throw new Exception("Formato del email $email erroneo");
            echo("<h2>Formato de email erroneo. prueba de nuevo</h2>");
        }
    }
    $archivo="registros.txt";

    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $nombre = $_POST["nombre"] ?? "";
        $mail = $_POST["mail"] ?? "";
        $edad = $_POST["edad"] ?? 0;
        $comentario = $_POST["comentario"] ?? "";
        if (isset($_POST["nombre"])) {
            try {
                validarEmail($mail);
                $fecha=date("Y-m-d H:i:s");
                $registro="$fecha|$nombre|$mail|$edad|$comentario". PHP_EOL;//guardamos si todo va bien el registro
                file_put_contents($archivo,$registro,FILE_APPEND);
            } catch (Exception $e) {
                $fecha=date("Y-m-d H:i:s");
                $error="$fecha | EJ29 | ".$e->getMessage()."| archivo.php | ";
                file_put_contents("error.log",$error, FILE_APPEND);//guardamos el error
            }
        }
    }


    ?>

</body>

</html>