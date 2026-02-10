<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="/ejercicio12MVC/app/vistas/style.css">
</head>

<body>

    <?php if (!empty($error)): ?>
        <div class="error"><?php echo htmlspecialchars($error) ?></div>
    <?php endif ?>
    <div class="tarjeta">
        <h2>Listado de cursos</h2>

        <?php if (empty($cursos)): ?>
            <p>No hay cursos todavía.</p>
        <?php else: ?>
            <table>
                <thead>
                    <tr>
                        <td>Nombre</td>
                        <td>Horas</td>
                    </tr>
                </thead>
                <tbody>
                    <?php foreach ($cursos as $c): ?>
                        <tr>
                            <td><?php echo htmlspecialchars($c->nombre) ?></td>
                            <td><?php echo htmlspecialchars($c->horas) ?></td>
                        </tr>
                    <?php endforeach ?>
                </tbody>
            </table>
        <?php endif ?>
    </div>


</body>

</html>