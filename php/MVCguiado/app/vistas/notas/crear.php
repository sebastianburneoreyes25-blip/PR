<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
<form action="index.php?accion=guardar" method="POST"><!--Enviamos el texto -->
<textarea name="texto" rows="4"><?php echo htmlspecialchars($antiguos['texto'] ?? ''); ?></textarea>

<br>

<input type="submit" value="Guardar"><br>
</form>
</body>
</html>