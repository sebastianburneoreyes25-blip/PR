<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejercicio 8</title>
</head>

<body>
    <h3>Bienvenido al conversor.</h3><br>
    <p>Selecciona una de las siguientes opciones dadas</p>
    <form action="ejercicio8.php" method="POST">
        <select name="conversor" style="margin-left: 3%;"><!--Creamos un selector para elegir que conversion queremos realizar-->
            <option value="dolarToEuro">Dolar a Euro</option>
            <option value="euroToDolar">Euro a Dolar</option>
            <option value="metroPies">Metros a Pies</option>
            <option value="piesMetro">Pies a Metros</option>
        </select>
        <br>
        <label>Unidades a Convertir</label>
        <br>
        <input type="number" min=0 step="0.01" name="valor"><!--Aqui seleccionaremos que cantidad a convertir-->
        <br>
        <input type="submit">
    </form>
    <?php
    $tipo = $_POST["conversor"] ?? "none"; //definimos las variables que usaremos como el valor del conversor para seleccionar una u otra operacion/formulas
    $valor = $_POST["valor"] ?? 0;
    $conversion = 0;
    $euroValue = 1; //pondremos de estandar el valior del euro
    $dolarValue = 0.86;
    $metro = 1; //pondremos de estandar el valor del metro
    $pies = 3.28;
    if ($tipo == "dolarToEuro") {
        $conversion = ($valor * 1) / 0.86;
        echo("<h4>$valor $ convertido a € es $conversion €</h4>");
    } elseif ($tipo == "euroToDolar") {
        $conversion = ($valor * 0.86) / 1;
        echo("<h4>$valor € convertido a $ es $conversion €</h4>");
    } elseif ($tipo == "metroPies") {
        $conversion = ($valor * 3.28) / 1;
        echo("<h4>$valor metros convertido a pies es $conversion pies</h4>");
    } elseif ($tipo == "piesMetro") {
        $conversion = ($valor * 1) / 3.28;
        echo("<h4>$valor pies convertido a metros es $conversion m</h4>");
    };
    
    ?>
</body>

</html>