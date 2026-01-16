<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Buscar</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container" >
<form action="search.php" method="POST">
<label>Nombre a buscar</label><br>
<input type="text" name="nombre"><br>
<input type="submit" value="Buscar" class="btn"><br>
</form>
<form action="index.php">
    <input type="submit" value="Volver a menu" class="btn">
</form>
</div>
<?php 

function comprobarAgenda($archivo){//funcion para comprobar que existen registros
    if(filesize($archivo)==0){
        echo("<h2>No hay contactos guardados.</h2>");
        throw new Exception("La lista de contactos está vacía");
    }

    if(!file_exists($archivo)){
            echo("<h2>No hay contactos guardados.</h2>");
            throw new Exception("El archivo $archivo no existe");
    }
}

if($_SERVER["REQUEST_METHOD"]=="POST"){
    try{
    $nombreBusqueda=$_POST["nombre"]??"";
    $archivo="agenda.txt";
    $encontrado=false;//boolean para expresion de tabla o mensaje
    comprobarAgenda($archivo);
    $lista=fopen($archivo,"r");
     $expresion="<table class='agenda-table'>
                    <thead>
                      <tr>
                          <th>Nombre</th>
                         <th>Teléfono</th>
                            </tr>
                       </thead>
                       <tbody>";
         while (($contacto = fgets($lista)) !== false){
            $contacto=trim($contacto);
            $contacto=str_replace(" ","",$contacto);

            if($contacto!=""){
                $arrayContacto=explode("|", $contacto);
            }
            if (str_contains(strtolower($arrayContacto[0]), strtolower($nombreBusqueda))){
            $expresion=$expresion."<tr>
            <td>".$arrayContacto[0]."</td>
            <td>". $arrayContacto[1]."</td>
             </tr>";//creacion de la tabla con el array contacto
             $encontrado=true;
        }
        }
        $expresion=$expresion."</tbody>
        </table>";

    }catch(Exception $e){
        $msgError="Error". $e->getMessage(). PHP_EOL;
        file_put_contents("error.log",$msgError,FILE_APPEND);
    }
}

?>
<?php
if($_SERVER["REQUEST_METHOD"]=="POST"){
if($encontrado==true){
echo($expresion);
}else{
    echo("<h2 style='text-align:center'>No hay resultados</h2>");
}
}
?>

</body>
</html>