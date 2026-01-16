<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <?php
    function comprobarAgenda($archivo){//Funcion comprobadora de que existe el archivo y/o no esta vacio
    if(filesize($archivo)==0){
        echo("<h2>No hay contactos guardados.</h2>");
        throw new Exception("La lista de contactos está vacía");
        }

        if(!file_exists($archivo)){
            echo("<h2>No hay contactos guardados.</h2>");
            throw new Exception("El archivo $archivo no existe");
        }
    }
    $archivo="agenda.txt";
    try{
        
        comprobarAgenda($archivo);
        $lista=fopen($archivo, "r");
        $contacto="";
        $expresion="<table class='agenda-table'>
                    <thead>
                      <tr>
                          <th>Nombre</th>
                         <th>Teléfono</th>
                            </tr>
                       </thead>
                       <tbody>";//Creamos tabla de expresion 
         
            while (($contacto = fgets($lista)) !== false){//Mientras contacto pueda coger una linea de la lista

      
            $contacto=trim($contacto);
            $contacto=str_replace(" ","",$contacto);
        
            if($contacto!=""){
                $arrayContacto=explode("|", $contacto);
            }
            $expresion=$expresion."<tr>
            <td>".$arrayContacto[0]."</td>
            <td>". $arrayContacto[1]."</td>
             </tr>";
        }
        $expresion=$expresion."</tbody>
        </table>";
    }catch(Exception $e){
        $msgError="Error". $e->getMessage(). PHP_EOL;
        file_put_contents("error.log",$msgError,FILE_APPEND);
    }
    ?>
    <div>
<?php 
    echo($expresion);
    ?>
    <form action="index.php" class="container">
    
    <input type="submit" class="btn" value="Volver a menu">
    </form>
</div>

</body>
</html>