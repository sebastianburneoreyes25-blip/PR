<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejercicio 15</title>
</head>

<body>

    <form action="ejercicio15.php" method="POST" style="text-align: center;"><!--Creamos un formulario para que elija una opcion, todos los botones tendran el mismo name  -->
        <label>
            <h2>Vamos a jugar, elige:</h2> <br>
        </label>
        <label> <input type="radio" value="Piedra" name="eleccion">Piedra </label>
        <label> <input type="radio" value="Papel" name="eleccion">Papel </label>
        <label> <input type="radio" value="Tijeras" name="eleccion">Tijeras </label><br>
        <input type="submit">

    </form>
<?php 
ini_set('display_errors',1);
error_reporting(E_ALL);
    $eleccion=$_POST["eleccion"]??"";//variables a tener en cuenta
    $posibilidades=["Piedra","Papel", "Tijeras"];
    $resultado=["Piedra"=>"Papel", "Papel"=>"Tijeras", "Tijeras"=>"Piedra"];
    $ganador="";
    if(isset($_POST["eleccion"])){//si se ha enviado algo se haran los siguientes procesos
        $cpuEleccion=$posibilidades[array_rand($posibilidades)];
        if($eleccion==$cpuEleccion){
            $ganador="Empate";
        }else{
            foreach($resultado as $gana=>$pierde){//recorremos el diccionario para elegie el ganador.
            if($eleccion==$gana and $cpuEleccion==$pierde){
                $ganador="Jugador";
            }elseif($eleccion==$pierde and $cpuEleccion==$gana){
                $ganador="CPU";
            }
        }
    }
    }
    echo("<h3>El ganador es $ganador</h3>");

?>
</body>

</html>