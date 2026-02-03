<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="/ejercicio11MVC/app/vistas/style.css">
</head>

<body>
    <?php if (!empty($error)): ?>
        <div class="error"><?php echo htmlspecialchars($error) ?></div>
    <?php endif; ?>
    <div class="tarjeta">
        <h2>Listado de alumnos</h2>

        <?php if (empty($alumnos)): ?>
            <p>No hay alumnos todavia</p>
        <?php else: ?>
            <table>
                <thead>
                    <tr>
                        <th>Fecha</th>
                        <th>Nombre</th>
                        <th>Email</th>
                        <th>Edad</th>
                        <th>Acciones</th>
                    </tr>
                </thead>
                <tbody>
                    <?php foreach ($alumnos as $a): ?>
                        <tr>
                            <td><?php echo htmlspecialchars($a->fechaCreacion); ?></td>
                            <td><?php echo htmlspecialchars($a->nombre); ?></td>
                            <td><?php echo htmlspecialchars($a->email); ?></td>
                            <td><?php echo htmlspecialchars($a->edad); ?></td>
                            <td>
                                <a href="/ejercicio11MVC/public/index.php?accion=borrar&id=<?php echo urlencode($a->id) ?>" 
                                onclick="return confirm ('¿seguro que quieres borrar este alumno?');">Borrar</a>
                            </td>
                        </tr>
                    <?php endforeach; ?>
                </tbody>
            </table>
        <?php endif; ?>
    </div>


</body>

</html>