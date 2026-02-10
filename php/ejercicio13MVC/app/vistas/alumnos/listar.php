<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="/ejercicio13MVC//app//vistas/style.css">
</head>

<body>
    <?php if (!empty($error)): ?>
        <div class="error"><?php echo htmlspecialchars($error) ?></div>
    <?php endif ?>
    <?php if (empty($alumnos)): ?>
        <div class="contenedor">No hay alumnos</div>
    <?php else : ?>
        <table>
            <thead>
                <tr>
                    <td>Fecha</td>
                    <td>Nombre</td>
                    <td>Email</td>
                    <td>Edad</td>
                </tr>
            </thead>
            <tbody>
                <?php foreach ($alumnos as $a): //$a sera el objeto alumno
                ?>
                    <tr>
                        <td><?php echo htmlspecialchars($a->fecha_creacion) ?></td>
                        <td><?php echo htmlspecialchars($a->nombre) ?></td>
                        <td><?php echo htmlspecialchars($a->email) ?></td>
                        <td><?php echo htmlspecialchars($a->edad) ?></td>
                    </tr>
                <?php endforeach ?>
            </tbody>
        </table>

    <?php endif ?>
</body>

</html>