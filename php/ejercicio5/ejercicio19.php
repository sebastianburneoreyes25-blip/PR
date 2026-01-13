<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejercicio 19</title>
</head>

<body>
    <form action="ejercicio19.php" method="POST"><!--Formulario donde introduciran los datos necesarios -->
        <h4>Validador de contraseñas</h4>
        <label>Usuario</label><br>
        <input type="text" name="user"><br>
        <label>Contraseña</label><br>
        <input type="password" name="pw"><br>
        <input type="submit" value="Comprobar">
    </form>
    <?php
    $password = $_POST["pw"] ?? "";//Variables necesarias
    $caracteresEsp = "@#";
    $user = $_POST["user"] ?? "";
    $valido = false;//bolean para determinar si es valida o no
    if (isset($_POST["pw"])) {
        if (strlen($password) >= 8) {//longitud de la contraseña minima de 8 caracteres
            if (str_contains($password, $user)) {//No puede estar el usuario en la contraseña
                $valido = false;
            } else {
                foreach (str_split($password) as $letra) {//str_split separa un str y lo convierte en array
                    if(str_contains($caracteresEsp, $letra)) {
                            $valido = true;
                    }
                }
            }
        }
        if ($valido == false) {
            echo ("<p>Contraseña no valida. Debe ser de minimo 8 caracteres y contener @ o #</p>");
        } else {
            echo ("<p>Contraseña valida</p>");
        }
    }

    ?>

</body>

</html>