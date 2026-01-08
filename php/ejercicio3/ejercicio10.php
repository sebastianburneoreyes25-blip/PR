<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejercicio 10</title>
</head>

<body>
    <form action="ejercicio10.php" method="POST"><!--Formulario para introducir el texto a analizar-->
        <h3>Analizador de texto</h3><br>
        <textarea name="texto" style="width: 30%;" rows="8"></textarea>
        <input type="submit">
    </form>
    <?php
    //Variables a tener en cuenta
    $textoCaracteres = $_POST["texto"] ?? "";
    $textoPalabras = explode(" ", $textoCaracteres); //Hacemos un array del texto en crudo quitando los espacios dejando solo las palabras.
    $totalCaracteres = 0;
    $totalPalbras = 0;
    $totalPHP = 0;
    $textoRever = strrev($textoCaracteres);
    if (isset($_POST["texto"])) {
        $totalCaracteres = strlen($textoCaracteres);//medimos la longitud del texto para los caracteres
        $totalPalbras = count($textoPalabras);//contamos cuantas palabras hay
        foreach ($textoPalabras as $palabra) {//bucle en el que iremos comprobando palabr a palabra las veces que sale php
            if ($palabra == "PHP" or $palabra == "php") {
                $totalPHP += 1;
            }
        }
    }
    
    echo ("<ul><li>Total de caracteres: $totalCaracteres </li>
    <li>Total de Palabras: $totalPalbras </li>
    <li>Texto al reves: $textoRever</li>
    <li>PHP en el texto: $totalPHP</li>")
    ?>
</body>
</html>