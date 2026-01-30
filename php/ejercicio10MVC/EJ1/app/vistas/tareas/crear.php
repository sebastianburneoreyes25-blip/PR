<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
        <link rel="stylesheet" href="../style.css">

</head>
<body>
    
<form action="index.php?accion=guardar" method="POST"><!--Enviamos el texto -->
<textarea name="titulo" rows="4"><?php echo htmlspecialchars($antiguos['titulo'] ?? ''); ?></textarea>

<br>

<input type="submit" value="Guardar"><br>
</form>
</body>
</html>