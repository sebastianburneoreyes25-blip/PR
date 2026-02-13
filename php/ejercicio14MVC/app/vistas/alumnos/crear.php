<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="/ejercicio14MVC/app/vistas/style.css">
</head>

<body>

    <?php
    $antiguos = $antiguos ?? ['nombre' => '', 'email' => '', 'edad' => ''];
    ?>

    <?php if (!empty($error)): ?>
        <div class="error"><?php echo htmlspecialchars($error); ?></div>
    <?php endif; ?>

    <div class="tarjeta">
        <h2>Formulario de alta</h2>

        <form method="POST" action="index.php?accion=guardar">

            <label>Nombre</label>
            <input type="text" name="nombre" value="<?php echo htmlspecialchars($antiguos['nombre']); ?>" required>

            <label>Email (opcional)</label>
            <input type="text" name="email" value="<?php echo htmlspecialchars($antiguos['email']); ?>">

            <label>Edad</label>
            <input type="text" name="edad" value="<?php echo htmlspecialchars($antiguos['edad']); ?>" required>

            <input type="submit" value="Guardar alumno">
        </form>
    </div>

</body>

</html>