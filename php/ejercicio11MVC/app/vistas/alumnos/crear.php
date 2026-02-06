<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="/ejercicio11MVC/app/vistas/style.css">
</head>

<body>
    <?php $antiguos = $antiguos ?? ['nombre' => '', 'email' => '', 'edad' => '']; ?>
    <?php if (!empty($error)): ?>
        <div class="error"><?php echo htmlspecialchars($error); ?></div>
    <?php endif; ?>
    <div class="tarjeta">
        <h2>Nuevo alumno</h2>

        <form action="/ejercicio11MVC/public/index.php?accion=guardar" method="POST">
            <label>Nombre (Min.3 caracteres) </label><br>
            <input type="text" name="nombre" required>
            <br>
            <label>Email (opcional)</label>
            <input type="text" name="email"  >

            <label>Edad (número entre 1 y 120)</label>
            <input type="text" name="edad"  required>

           <input type="submit" value="Guardar Alumno">
        </form>
    </div>


    </form>
    </div>
</body>

</html>