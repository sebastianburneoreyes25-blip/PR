<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejercicio 5</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>
<body>
    <form action="ejercicio5.php" method="POST" style="margin-left: 5%;"><!-- Creo el formulario que recogera los comentarios de los usuarios-->
        <label>ESCRIBE TU COMENTARIO</label><br>
        <textarea name="cajaComentario" style="width: 50%; "></textarea><br>
        <input type="submit">
    </form>
    <?php
    $comentario = $_POST["cajaComentario"] ?? "No hay comentarios disponibles";//Aqui recibira lo escrito anteriormente en el texarea
    $palabrotas = ["tonto", "feo", "idiota", "loco"];//palabras a censurar
    $array = explode(" ", $comentario);//convertimos en array el comentario creando elementos separados por un espacio en blanco
    foreach ($array as $palabra) {//bucle para comprobar cada palabra del copmentario con las palabras a censurar
        foreach ($palabrotas as $taco) {
            if ($palabra == $taco) {
                $censor = str_repeat("*", strlen($palabra));//creamos una palabra censurada con la misma longitud que la palabra sin censura
                $comentario = str_replace($palabra, $censor, $comentario);//remplazamos en el comentario la palabra sin censura por los *
            }
        }
    }
    ?>
    <div class="row" style="margin-left:4%"><!--Creamos con Boostrap una card para los comentarios -->
        <div class="card; col-9" style="width: 600px; text-align: center;">
            <div class="card-header; shadow-lg">
                <h4>Comentarios</h4>
            </div>
            <div class="card-body; shadow-lg ">
                <div class="card-text;shadow-lg ">
                    <p><?php echo ($comentario) ?></p>
                </div>
            </div>
        </div>
        <div class="col-3"></div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</body>
</html>