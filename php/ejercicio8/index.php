<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejercicio 31 </title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container"><!--Menu con clase descrita en el archivo css. Cada boton nos llevara a un formulario diferente de php-->
    <h2>Menu</h2><br>
<form action="add_contacto.php">
<input type="submit" value="Añadir contacto" class="btn"><br>
</form>    

<form action="lista_agenda.php">
<input type="submit"value="Agenda" class="btn"><br>
</form>

<form action="search.php">
    <input type="submit" value="Buscar" class="btn"><br>
</form>

</div>
</body>
</html>