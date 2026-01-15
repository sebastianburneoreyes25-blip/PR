<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejercicio 24</title>
</head>
<body>

<?php 
function leerArchivoSeguro($archivo){//definimos la funcion de leer archivo de manera segura
        if(!file_exists($archivo)){//si no existe, lanzara la excepcion descrita
            throw new Exception("El archivo $archivo no existe");
        }
        if(!is_readable($archivo)){//si no se puede leer, lanzara la excepcion descrita
            throw new Exception("El archivo $archivo no se puede leer");
        }
        
        $contenido=file_get_contents($archivo);//coge el contenido del archivo y lo devuelve en la variable contenido
        return $contenido;
}

try{//Comprobamos de manera segura que se pueda hacer lo descrito dentro
    $contenido=leerArchivoSeguro("notas.txt");//intentamos leer el archivo notas.txt
    echo("<p>$contenido</p>");
}catch(Exception $e){
    $fecha=date("Y-m-d H:i:s");//Registramos la fecha en la que se produjo el error
    $mensaje="[$fecha]  Error:".$e->getMessage().PHP_EOL;//Creamos el mensaje de error. Con getMessage() cogeremos el mensaje enviado en el throw.
    file_put_contents("error.log",$mensaje,FILE_APPEND);//Enviamos el error al archivo error.log.
}



?>

</body>
</html>