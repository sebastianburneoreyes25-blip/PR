<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
<?php

$notas=new RepositorioNotas;
$notasArray=$notas->obtenerTodas();
if(empty($notasArray)){
    echo "<h2>No hay notas :(</h2>";
}

foreach($notasArray as $nota){
    echo "<p>Nota:". $nota->texto. "</p><p>Fecha: $nota->fecha<br>";
}

?>

</body>
</html>