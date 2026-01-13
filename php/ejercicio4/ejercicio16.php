<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejercicio 16</title>
</head>

<body>
    <h1>Generador de mails automatico.</h1><!--Pedimos los datos -->
    <form action="ejercicio16.php" method="POST">
        <label>Nombre</label><br>
        <input type="text" name="nombre"><br>
        <label>Apellidos</label><br>
        <input type="text" name="apellidos"><br>
        <label>Dominio</label><br>
        <input type="text" name="dominio"><br>
        <input type="submit">
    </form>

    <?php
    //variables a tener en cuenta
    $nombre = $_POST["nombre"] ?? "";
    $apellidos = $_POST["apellidos"] ?? "";
    $dominio = $_POST["dominio"] ?? "";
    $inicioUrl = array('http://', 'https://', 'ftp://', 'www.');
    if (isset($_POST["nombre"])) {
        $correo = substr($nombre, 0, 1); //Cogemos solo la primera letra del string
        $apellidos = trim($apellidos); //con Trim y str_replace quitamos los espacios en blanco que pueda haber en los apellidos
        $apellidos = str_replace(" ", "", $apellidos);
        $correo = $correo . strtolower($apellidos) . "@"; //unimos la primera letra con los apellidos enteros en minusculas.
        $urlLimpia = explode('/', str_replace($inicioUrl, '', $dominio));/*limpiamos la url para quedarnos solo con l aparte importante, (el nombre de la empresa 
   supuestamente)quitando el incio de la URL(anteriormente definido en inicioUrl) y creando un array donde cada clave será definida despues de cada / */
        $correo = $correo . $urlLimpia[0]; //escogemso la primera clave del array que sera en un inicio el dominio(empresa.com/es)
        $correo = trim($correo);
        $correo = strtolower($correo);
        echo ("$correo");
    }

    ?>

</body>

</html>