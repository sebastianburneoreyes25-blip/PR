<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejercicio 25</title>
</head>

<body>
    <form action="EJ25.PHP" method="POST"><!--Formulario para pedir el user y mail a giuardar-->
        <label>Nombre</label><br>
        <input type="text" name="name"><br>
        <label>Mail</label><br>
        <input type="mail" name="mail"><br>
        <input type="submit" value="Guardar">
    </form>

    <?php
    if($_SERVER["REQUEST_METHOD"]=="POST"){//Si hay post
    $usuario = $_POST["name"]??"";
    $mail = $_POST["mail"]??"";//recogemos datos, entre ellos la fecha
    $fecha=date("Y-m-d H:i:s");


    try {
        if(empty(trim($usuario))){//si el usuario esta vacio lanza error
            throw new Exception("Usuario vacio");
        }
        if(!str_contains($mail,"@")){//si el mail no contiene @ lanza error
            throw new Exception("El mail '$mail' no es valido. No contiene @.");
        }
        $registro="$fecha| $usuario| $mail".PHP_EOL;//si no ha habido error se ejecuta el registro para añadir a usuarios,txt

        file_put_contents("usuarios.txt", $registro, FILE_APPEND);
        echo("Usuario guardado correctamente");

    } catch (Exception $e) {

        $mensajeError="$fecha Error:". $e->getMessage(). PHP_EOL;//si falla, guardamos el mensaje con la fecha y enviamos a error.log
        file_put_contents("error.log",$mensajeError,FILE_APPEND);
        echo("ERROR: Usuario no guardado");
    }
    }
    ?>
</body>

</html>