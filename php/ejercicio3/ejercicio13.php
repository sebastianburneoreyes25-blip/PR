<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejercicio 13</title>
</head>
<body>
    <h2>Introduce numeros separados por comas</h2>
    <form action="ejercicio13.php" method="POST">
    <textarea name="texto" rows="5"></textarea><!--Introduciran los numeros-->
    <input type="submit">
    </form>
    <?php 
    $texto=$_POST["texto"]??"";
    $numeros=explode(",",$texto);//Quitamos las comas y convertimos en array
    $numeros=array_map("trim",$numeros);
    sort($numeros, SORT_NUMERIC);//Aqui introduciremos los numeros ordenados
    $lista="<ol>";
    foreach($numeros as $numero){
        $lista=$lista."<li>$numero</li>";
    }
    $lista=$lista."</ol>";
    echo($lista);
    

    
    ?>
</body>
</html>