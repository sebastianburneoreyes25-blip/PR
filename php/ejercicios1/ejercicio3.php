<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <?php
    $productos = ["Caja de manzanas" => 5.5, "Puerro unidad" => 0.68, "Bolsa de Naranajas" => 4.5, "Bandeja de pollo" => 7.6];
    $formulario = "";
    foreach ($productos as $producto => $precio) {
        $formulario = $formulario . "<label>$producto</label> <input type='number' name='$producto._Cantidad'><br><br>";
    }
    $compra = $_POST["eleccionProductos"] ?? "";

    ?>


    <form action="ejercicio3.php" method="POST">


        <?php echo $formulario ?>
        <input type="submit">
    </form> 


</body>

</html>