<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <?php
    //aqui definimos las variables necesarias para despues
    $tabla = '';
    $productos = ["CajaDeManzanas" => 5.5, "PuerroUnidad" => 0.68, "BolsaDeNaranajas" => 4.5, "BandejaDePollo" => 7.6];
    $formulario = "";
    $totalCompra=0;
    foreach ($productos as $producto => $precio) {  //recorremos la lista de productos detallando producto  precio
        $productoCantidad = (int)($_POST['cantidad'][$producto] ??0);
        //por cada ciclo del bucle, creara un apartado donde añadir a la lista x unidades de productos
        $formulario = $formulario . "<label>$producto</label> <input type='number' min='0' name='cantidad[$producto] value='$productoCantidad'><br><br>";
        $totalProducto = $precio * $productoCantidad;
        //Creara de manera automatica la tabla por cantidad de productos 
        $tabla = $tabla."<tr><td>$producto</td><td>$productoCantidad</td><td>$totalProducto.'€'</td></tr>";
        $totalCompra+=$totalProducto;//suma el total de los productos comprados
    }

    ?>


    <form action="ejercicio3.php" method="POST"><!--Recargará la pagina al hacer submit-->


        <?php echo $formulario ?>
        <input type="submit">
    </form>
    <table border="2"><!--Aqui la tabla y lo que se creo de manera automatica en el bucle-->
        <tr>
            <td>
                Producto
            </td>
            <td>Cantidad</td>
            <td>Total</td>
        </tr>
        <?php echo $tabla
        ?>
<tr><td>Total a pagar</td><td colspan="2"><?php echo $totalCompra.'€'?></tr>
    </table>

</body>

</html>