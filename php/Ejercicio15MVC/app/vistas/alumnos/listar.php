<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="/Ejercicio15MVC/app/vistas/style.css">
</head>

<body>
    <?php if (!empty($error)): ?>
        <div class="error"> <?php echo htmlspecialchars($error) ?></div>
    <?php endif ?>
    <?php if (!empty($alumnos)): ?>
        <div class="contenedor">
            <table>
                <thead>
                    <tr>
                        <td>ID</td>
                        <td>Nombre</td>
                        <td>Email</td>
                        <td>Edad</td>
                        <td>¿Borrar?</td>
                    </tr>
                </thead>
                <tbody>


                    <?php foreach ($alumnos as $a): ?>

                        <tr>
                            <td><?php echo htmlspecialchars($a->id) ?> </td>
                            <td><?php echo htmlspecialchars($a->nombre) ?></td>
                            <td><?php echo htmlspecialchars($a->email) ?></td>
                            <td><?php echo htmlspecialchars($a->edad) ?></td>
                            <td><button><a href="/Ejercicio15MVC/public/index.php?accion=borrar&id=<?php 
                            echo htmlspecialchars($a->id)?>" onclick="return confirm('¿Estás seguro de que deseas eliminar a este alumno?')">Borrar</a></button></td>
                            <!-- Aquí es donde realmente mandara el id a borrar.-->
                        </tr>
                    <?php endforeach ?>
                </tbody>
            </table>
        </div>
        <?php else: ?>
            <div class="tarjeta">Lista vacía</div>
    <?php endif ?>
</body>

</html>