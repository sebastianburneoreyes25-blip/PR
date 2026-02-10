<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="/ejercicio12MVC/app/vistas/style.css">
</head>
<body>
    <?php if(!empty($error)): ?>
        <div class="error"><?php htmlspecialchars($error)?></div>
    <?php endif ?>
    <div class="tarjeta">
        <h2>Nuevo Cursos</h2>
        <form action="/ejercicio12MVC/public/index.php?accion=guardar" method="POST">
            <label >Nombre del curso </label>
            <input type="text" name="nombre" value="<?php echo htmlspecialchars($antiguos['nombre'])?>" required>
            <label>Horas del curso</label>
            <input type="text" name="horas" value="<?php echo htmlspecialchars($antiguos['horas']) ?>">
            <input type="submit" value="Guardar">

        </form>

    </div>
</body>
</html>