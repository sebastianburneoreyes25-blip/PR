<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="/ejercicio11MVC/app/vistas/style.css">
</head>
<body>
    <?php $antiguos= $antiguos??['nombre'=>'', 'email'=>'','edad'=>'' ]; ?>
    <?php if(!empty($error)):?>
        <div class="error"><?php echo htmlspecialchars($error);?></div>
        <?php endif;?>
        <div class="tarjeta">
            <h2>Nuevo alumno</h2>

            <form action="/ejercicio11MVC/public/index.php?accion=guardar" method="POST">
            <label>Nombre (Min.3 caracteres) </label><br>
            <input type="text" name="nombre" value="<?php echo htmlspecialchars($antiguos['nombre']);?>" required>
            <br>


            </form>
        </div>
</body>
</html>