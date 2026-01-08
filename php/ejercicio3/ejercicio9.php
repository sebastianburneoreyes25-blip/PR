<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejercicio 9</title>
</head>

<body>
    <H1 style="text-align:center">PIZZERIA XAMMP</H1>
    <form action="ejercicio9.php" method="POST" style="text-align:center"><!--Creamos las opciones de la pizza(tipo,ingredientes....)-->
        <label name="pizza">Elige el tamaño de la pizza: <br>
            <input type="radio" name="tamaño" value="Pequeña">Pequeña: 5€<br>
        </label>
        <label name="pizza">
            <input type="radio" name="tamaño" value="Mediana">Mediana: 10€<br>
        </label>
        <h2>Ingredientes (1€/u):</h2>
        <label>
            <input type="checkbox" name="ingredientes[]" value="Jamón">Jamón
        </label>
        <label>
            <input type="checkbox" name="ingredientes[]" value="Queso">Queso
        </label>
        <label>
            <input type="checkbox" name="ingredientes[]" value="Piña">Piña
        </label>
        <label>
            <input type="checkbox" name="ingredientes[]" value="Pimientos">Pimientos

        </label><br>
        <input type="submit">
    </form>
    <?php
    $size=$_POST["tamaño"]??"none";//Variables a tener en cuenta 
    $ingredientes=$_POST["ingredientes"]??[];
    $total=0;
    $totalIngr=0;
    $lista="<ul>Ingredientes:";
    $precioTamaño=0;
    if(isset($_POST["ingredientes"])){//si hay algo enviado se hara las siguientes operaciones
        if($size=="Pequeña"){//Determinamos el tamaño, precio(para despues expresarlo) y el añadimos al total
            $total+=5;
            $precioTamaño=5;
        }elseif($size=="Mediana"){
            $total+=10;
            $precioTamaño=10;
        };
        $totalIngr=count($ingredientes);//Contamos la cantidada de ingrtedientes que hay para añadirlo al total
        $total+=$totalIngr;
        foreach($ingredientes as $ingrediente){//añadimos el codigo HTML de la lista y sus valores para despes expresarlo.
            $lista=$lista."<li>$ingrediente : 1€</li>";
            
        }
        $lista=$lista."</ul>";
        echo("<h4>Pizza $size : $precioTamaño €</h4><br>$lista <br><br><h3>Total= $total €");
    }
    ?>
</body>

</html>